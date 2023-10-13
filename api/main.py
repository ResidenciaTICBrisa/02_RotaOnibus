from fastapi import FastAPI
from pydantic import BaseModel
import osmnx as ox
import networkx as nx
import pickle

app = FastAPI()

class BusStop(BaseModel):
    lat: float
    lon: float

# Modelo Pydantic atualizado
class InputData(BaseModel):
    current_location: BusStop
    destiny_location: BusStop
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
    all_stops = [
    {
        "id_stop": 7907,
        "lat": -15.963291999999997,
        "lon": -48.022833000000006,
        "linha": "0.205"
    },
    {
        "id_stop": 7908,
        "lat": -15.959593999999997,
        "lon": -48.026028,
        "linha": "0.205"
    },
    {
        "id_stop": 6350,
        "lat": -15.95956741758501,
        "lon": -48.02601882854514,
        "linha": "0.205"
    },
    {
        "id_stop": 3809,
        "lat": -15.956576488628638,
        "lon": -48.02855193528977,
        "linha": "0.255"
    },
    {
        "id_stop": 3810,
        "lat": -15.953939223131423,
        "lon": -48.030795914341546,
        "linha": "0.205"
    },
    {
        "id_stop": 6354,
        "lat": -15.95117649533479,
        "lon": -48.03315367341592,
        "linha": "0.205"
    },
    {
        "id_stop": 7909,
        "lat": -15.948016999999997,
        "lon": -48.03582800000001,
        "linha": "0.205"
    },
    {
        "id_stop": 3811,
        "lat": -15.9480060886309,
        "lon": -48.03584505006028,
        "linha": "0.205"
    },
    {
        "id_stop": 7910,
        "lat": -15.943535999999998,
        "lon": -48.039344,
        "linha": "0.205"
    },
    {
        "id_stop": 3813,
        "lat": -15.938393849213748,
        "lon": -48.04209305412461,
        "linha": "0.205"
    },
    {
        "id_stop": 7911,
        "lat": -15.938388999999995,
        "lon": -48.042086,
        "linha": "0.205"
    },
    {
        "id_stop": 7912,
        "lat": -15.933691999999997,
        "lon": -48.0437,
        "linha": "0.255"
    },
    {
        "id_stop": 3814,
        "lat": -15.9336829394337,
        "lon": -48.043679856954,
        "linha": "0.255"
    },
    {
        "id_stop": 7913,
        "lat": -15.925732999999996,
        "lon": -48.046239,
        "linha": "0.255"
    },
    {
        "id_stop": 3816,
        "lat": -15.920460708461938,
        "lon": -48.04791146325488,
        "linha": "0.255"
    },
    {
        "id_stop": 7914,
        "lat": -15.920452999999997,
        "lon": -48.047928,
        "linha": "0.255"
    },
    {
        "id_stop": 7915,
        "lat": -15.917502999999998,
        "lon": -48.048872,
        "linha": "0.205"
    },
    {
        "id_stop": 3817,
        "lat": -15.917478165997663,
        "lon": -48.048870808929316,
        "linha": "0.205"
    },
    {
        "id_stop": 7917,
        "lat": -15.908972,
        "lon": -48.051611,
        "linha": "0.255"
    },
    {
        "id_stop": 7922,
        "lat": -15.891674999999996,
        "lon": -48.057164,
        "linha": "0.205"
    },
    {
        "id_stop": 7923,
        "lat": -15.891674999999996,
        "lon": -48.057164,
        "linha": "0.205"
    },
    {
        "id_stop": 5391,
        "lat": -15.874655767236849,
        "lon": -48.0394544647222,
        "linha": "0.205"
    },
    {
        "id_stop": 4975,
        "lat": -15.872196498773105,
        "lon": -48.02948710262496,
        "linha": "0.205"
    },
    {
        "id_stop": 4976,
        "lat": -15.867699286908332,
        "lon": -48.031872129100485,
        "linha": "0.205"
    }
]

    # 1. Rota de Baldeação (Caminhada)
    start_point = (data.current_location.lat, data.current_location.lon)

    first_stop = all_stops[0]
    end_point = (first_stop["lat"], first_stop["lon"])

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota de baldeação
    baldeacao_coords = calculate_route(start_point, end_point, G)

    # 2. Rota Veicular
    G_DF = ox.load_graphml("drive_true_distrito_federal.graphml")

    nearest_nodes = [ox.distance.nearest_nodes(G_DF, stop["lon"], stop["lat"]) for stop in all_stops]

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