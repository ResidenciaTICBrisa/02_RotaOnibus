from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import osmnx as ox
import networkx as nx
import pickle
import math

app = FastAPI()

# Definição do modelo Pydantic para entrada


class Coordinates(BaseModel):
    lat_origin: float
    lon_origin: float


# Carregando o grafo das paradas de ônibus
with open('bus_stops_graph.pkl', 'rb') as f:
    bus_stops_graph = pickle.load(f)

# Função para calcular a distância haversine


def haversine(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    R = 6371000  # raio da Terra em metros
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * \
        math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    meters = R * c
    return meters

# Função para encontrar a parada de ônibus mais próxima


def find_nearest_stop(coord, graph):
    nearest_stop = None
    nearest_distance = float('inf')
    for node, attributes in graph.nodes(data=True):
        stop_coord = (attributes['lat'], attributes['lon'])
        distance = haversine(coord, stop_coord)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_stop = node
    return graph.nodes[nearest_stop]['lat'], graph.nodes[nearest_stop]['lon']

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


@app.post('/calculate_route', tags=['Route'], summary='Calcula a rota até a parada de ônibus mais próxima')
async def get_route(coordinates: Coordinates):
    start_point = (coordinates.lat_origin, coordinates.lon_origin)

    # Encontrar a parada de ônibus mais próxima usando o grafo das paradas de ônibus
    end_point = find_nearest_stop(start_point, bus_stops_graph)

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota
    route_coords = calculate_route(start_point, end_point, G)

    return {"baldeacao": route_coords}


@app.post('/paradas/',
          tags=['Paradas'],
          summary='Calcula e retorna as paradas ao longo do caminho',
          description='''Este endpoint aceita coordenadas de origem e destino e retorna as paradas necessárias para a realização do trajeto.
          - `lat_origin`: Latitude da origem (entre -90 e 90)
          - `lon_origin`: Longitude da origem (entre -180 e 180)
          - `lat_destination`: Latitude do destino (entre -90 e 90)
          - `lon_destination`: Longitude do destino (entre -180 e 180)'''
          )
async def get_coordinates(coordinates: Coordinates):
    if not (-90 <= coordinates.lat_origin <= 90):
        raise HTTPException(
            status_code=400, detail="Latitude de origem inválida. Deve ser entre -90 e 90.")

    if not (-180 <= coordinates.lon_origin <= 180):
        raise HTTPException(
            status_code=400, detail="Longitude de origem inválida. Deve ser entre -180 e 180.")

    if not (-90 <= coordinates.lat_destination <= 90):
        raise HTTPException(
            status_code=400, detail="Latitude de destino inválida. Deve ser entre -90 e 90.")

    if not (-180 <= coordinates.lon_destination <= 180):
        raise HTTPException(
            status_code=400, detail="Longitude de destino inválida. Deve ser entre -180 e 180.")

    # Simulação de paradas como uma lista de dicionários
    paradas = [
        {'nome': 'Parada 1', 'coordenadas': [40.712776, -74.005974]},
        {'nome': 'Parada 2', 'coordenadas': [34.052235, -118.243683]},
        {'nome': 'Parada 3', 'coordenadas': [41.878113, -87.629799]},
        {'nome': 'Parada 4', 'coordenadas': [42.878113, -88.629799]},
        {'nome': 'Parada 5', 'coordenadas': [43.878113, -89.629799]},
        {'nome': 'Parada 6', 'coordenadas': [44.878113, -90.629799]},
    ]

    return {'origin': [coordinates.lat_origin, coordinates.lon_origin],
            'destination': [coordinates.lat_destination, coordinates.lon_destination],
            'paradas': paradas}
