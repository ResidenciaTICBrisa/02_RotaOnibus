from fastapi import FastAPI
from pydantic import BaseModel
import osmnx as ox
import networkx as nx
import pickle
from typing import List

app = FastAPI()

# Definição do modelo Pydantic para entrada
class Coordinates(BaseModel):
    lat_origin: float
    lon_origin: float

class BusStop(BaseModel):
    lat: float
    lon: float

# Modelo Pydantic atualizado
class InputData(BaseModel):
    current_location: BusStop
    paradas: List[BusStop]

# Carregando o grafo das paradas de ônibus
with open('grafoDirecional.grafo', 'rb') as f:
    bus_stops_graph = pickle.load(f)

# Função para calcular e desenhar a rota de caminhada
def calculate_route(start_point, end_point, graph):
    nearest_start = ox.distance.nearest_nodes(
        graph, X=[start_point[1]], Y=[start_point[0]])[0]
    nearest_end = ox.distance.nearest_nodes(
        graph, X=[end_point[1]], Y=[end_point[0]])[0]
    route = nx.shortest_path(graph, nearest_start,
                             nearest_end, weight='length', method='dijkstra')
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x'])
                    for node in route]
    return route_coords

@app.get('/', tags=['Root'], summary='Verifica se o servidor está rodando')
async def root():
    return {'Servidor rodando!'}

@app.post('/calculate_route', tags=['Route'], summary='Calcula as rotas de baldeação e veicular')
async def get_route(data: InputData):
    # 1. Rota de Baldeação (Caminhada)
    start_point = (data.current_location.lat, data.current_location.lon)
    # Pegue a primeira parada de ônibus da lista
    first_bus_stop = data.paradas[0]
    end_point = (first_bus_stop.lat, first_bus_stop.lon)

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota de baldeação
    baldeacao_coords = calculate_route(start_point, end_point, G)

    # 2. Rota Veicular
    G_DF = ox.load_graphml("private_false_distrito_federal.graphml")

    # Começando da primeira parada de ônibus e seguindo para as outras paradas
    all_stops = data.paradas

    nearest_nodes = [ox.distance.nearest_nodes(
        G_DF, stop.lon, stop.lat) for stop in all_stops]

    all_routes = []
    for i in range(len(nearest_nodes) - 1):
        route_segment = nx.shortest_path(
            G_DF, nearest_nodes[i], nearest_nodes[i + 1], weight='length')
        all_routes.extend(route_segment[:-1])
    all_routes.append(nearest_nodes[-1])

    veicular_coords = [(G_DF.nodes[node]['y'], G_DF.nodes[node]['x'])
                       for node in all_routes]

    return {
        "baldeacao": baldeacao_coords,
        "rota_veicular": veicular_coords
    }
