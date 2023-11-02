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


@app.get('/', tags=['Root'], summary='Verifica se o servidor está rodando')
async def root():
    return {'Servidor rodando!'}


@app.post('/calculate_route', tags=['Route'], summary='Calcula as rotas de baldeação e veicular')
async def get_route(data: InputData):
  
    # 1. Rota de Baldeação (Caminhada) até Origem
    ## --------------------------------------------------------------------

    start_point = (data.current_location.lat, data.current_location.lon)
    dest_point = (data.destiny_location.lat, data.destiny_location.lon)

    # Mapear origem e destino para os nós no Grafo das Linhas e Paradas
    ## Ler o grafo de um arquivo usando pickle
    with open('grafoParadas.grafo', 'rb') as f:
        G_Paradas = pickle.load(f)

    nos_origem = rt.calculaNosProximos(G_Paradas, start_point[1], start_point[0])
    no_destino = rt.calculaNoProximo(G_Paradas, dest_point[1], dest_point[0])

    paradas, linhas_usadas = rt.calculaRotaOtima(G_Paradas, nos_origem, no_destino)

    if len(paradas) == 0:
        nos_destino = rt.calculaNosProximos(G_Paradas, dest_point[1], dest_point[0])
        paradas, linhas_usadas = rt.calculaRotaOtimaNx(G_Paradas, nos_origem, nos_destino)

    paradas_info_json = rt.paradasELinhasToJson(G_Paradas, paradas, linhas_usadas)

    first_stop = paradas_info_json[0]
    end_point = (first_stop["lat"], first_stop["lon"])

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G_Origem = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota de baldeação
    baldeacao_coords_orig = rt.calculaRotaCaminhada(start_point, end_point, G_Origem)


    # 2. Rota Veicular
    ## --------------------------------------------------------------------
    
    G_DF = ox.load_graphml("leve_distrito_federal.graphml")

    nearest_edges = [ox.distance.nearest_edges(G_DF, stop["lon"], stop["lat"]) for stop in paradas_info_json]

    # Pegando o primeiro nó de cada aresta encontrada para roteamento
    nearest_nodes_from_edges = [edge[0] for edge in nearest_edges]

    all_routes = []
    for i in range(len(nearest_nodes_from_edges) - 1):
        route_segment = nx.shortest_path(
            G_DF, nearest_nodes_from_edges[i], nearest_nodes_from_edges[i + 1], weight='length')
        all_routes.extend(route_segment[:-1])
    all_routes.append(nearest_nodes_from_edges[-1])

    veicular_coords = [(G_DF.nodes[node]['y'], G_DF.nodes[node]['x'])
                    for node in all_routes]
    

    # 3. Rota de Baldeação (Caminhada) até Destino
    ## -------------------------------------------------------------------- 

    last_stop = paradas_info_json[len(paradas_info_json) - 1]
    start_point = (last_stop["lat"], last_stop["lon"])

    # Baixar o mapa da área de interesse para cálculo da rota de caminhada
    G_Destino = ox.graph_from_point(start_point, dist=2000, network_type='walk')

    # Calcular a rota de baldeação
    baldeacao_coords_dest = rt.calculaRotaCaminhada(start_point, dest_point, G_Destino)
    
    return {
        "baldeacao_orig": baldeacao_coords_orig,
        "rota_veicular": veicular_coords,
        "baldeacao_dest": baldeacao_coords_dest,
        "paradas": paradas_info_json
    }