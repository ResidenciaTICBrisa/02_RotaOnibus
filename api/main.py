from fastapi import FastAPI
from pydantic import BaseModel
import osmnx as ox
import networkx as nx
import pickle
import roteamento as rt
import time

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
  
    # 1. Rota de Baldeação (Caminhada) até Origem
    ## --------------------------------------------------------------------
    tempo_inicial = time.time()

    start_point = (data.current_location.lat, data.current_location.lon)
    dest_point = (data.destiny_location.lat, data.destiny_location.lon)

    # Mapear origem e destino para os nós no Grafo das Linhas e Paradas
    ## Ler o grafo de um arquivo usando pickle
    with open('grafoDirecional.grafo', 'rb') as f:
        G_Direcional = pickle.load(f)

    nos_origem = rt.calculaNosProximos(G_Direcional, start_point[1], start_point[0])
    no_destino = rt.calculaNoProximo(G_Direcional, dest_point[1], dest_point[0])

    paradas, linhas_usadas = rt.calculaRotaOtima(G_Direcional, nos_origem, no_destino)

    # Teste sem paradas próximas umas das outras
    # paradas = [7672, 7907, 7908, 3809, 3810, 6354, 7909, 7910, 3813, 7912, 7913, 3816, 7915, 7917, 7923, 5391, 4975, 4976]
    # linhas_usadas = [None, '0.205', '0.205', '0.205', '0.205', '0.205', '0.205', '0.205', '0.255', '0.255', '0.205', '0.205', '0.255', '0.205', '0.205', '0.205', '0.205', '0.205']

    # Teste com poucas paradas: 3 paradas e 2 linhas
    # paradas = [7672, 7907, 7908]
    # linhas_usadas = [None, '0.205', '0.205']

    paradas_info_json = rt.paradasELinhasToJson(G_Direcional, paradas, linhas_usadas)

    first_stop = paradas_info_json[0]
    end_point = (first_stop["lat"], first_stop["lon"])

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota de baldeação
    baldeacao_coords_orig = calculate_route(start_point, end_point, G)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial
    print(f"Rota até Origem: {tempo_total}")

    # 2. Rota Veicular
    ## --------------------------------------------------------------------

    tempo_inicial = time.time()
    
    G_DF = ox.load_graphml("drive_true_distrito_federal.graphml")

    print(len(paradas_info_json))

    nearest_nodes = [ox.distance.nearest_nodes(G_DF, stop["lon"], stop["lat"]) for stop in paradas_info_json]

    all_routes = []
    for i in range(len(nearest_nodes) - 1):
        route_segment = nx.shortest_path(
            G_DF, nearest_nodes[i], nearest_nodes[i + 1], weight='length')
        all_routes.extend(route_segment[:-1])
    all_routes.append(nearest_nodes[-1])

    veicular_coords = [(G_DF.nodes[node]['y'], G_DF.nodes[node]['x'])
                       for node in all_routes]
    
    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial
    print(f"Rota Veicular: {tempo_total}")

    # 3. Rota de Baldeação (Caminhada) até Destino
    ## -------------------------------------------------------------------- 

    tempo_inicial = time.time()

    last_stop = paradas_info_json[len(paradas_info_json)-1]
    start_point = (last_stop["lat"], last_stop["lon"])

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota de baldeação
    baldeacao_coords_dest = calculate_route(start_point, dest_point, G)

    tempo_final = time.time()
    tempo_total = tempo_final - tempo_inicial
    print(f"Rota até Destino: {tempo_total}")
    
    return {
        "baldeacao_orig": baldeacao_coords_orig,
        "rota_veicular": veicular_coords,
        "baldeacao_dest": baldeacao_coords_dest
    }