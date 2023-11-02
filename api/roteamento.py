import heapq
import networkx as nx
import osmnx as ox
from geopy.distance import geodesic
from shapely.geometry import Point
import signal

# Peso (PESO) para dificultar a baldeação das linhas ônibus e aplicar no algoritmo.
PESO = 10
# Raio para eliminar paradas muito próximas umas das outras
RAIO_PARADAS_PROXIMAS = 0.009
# Maximo de Linhas de tamanho 20 
MAX_LINHAS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
LEN_MAX_LINHAS = 20
# Tempo para calcular menor rota de cada no_origem, em segundos
SECONDS = 5
RESET = 0
# Dijkstra: indice da primeira linha de ônibus na lista 
IDX_PRIMEIRA_LINHA = 0
minHeap = []


def calculaNoProximo(G, long, lat):
    distancias = {}
    ponto = Point(long, lat)
    for node in G.nodes():
        node_coords = Point(G.nodes[node]['coords'])  
        dist = node_coords.distance(ponto)
        distancias[node] = {'dist': dist}
    # Find the nodes with the shortest distancias to the origin and destination
    noMaisPerto = min(distancias, key=lambda x: distancias[x]['dist'])
    return noMaisPerto


def calculaNosProximos(G, long, lat, raio=0.007):
    nos_proximos = []
    ponto = Point(long, lat)
    for node in G.nodes():
        node_coords = Point(G.nodes[node]['coords'])
        dist = node_coords.distance(ponto)
        if dist <= raio:
            nos_proximos.append(node)
    return nos_proximos


def calculaRotaCaminhada(start_point, end_point, graph):
    nearest_start = ox.distance.nearest_nodes(
        graph, X=[start_point[1]], Y=[start_point[0]])[0]
    nearest_end = ox.distance.nearest_nodes(
        graph, X=[end_point[1]], Y=[end_point[0]])[0]
    route = nx.shortest_path(graph, nearest_start,
                             nearest_end, weight='length', method='dijkstra')
    route_coords = [(graph.nodes[node]['y'], graph.nodes[node]['x'])
                    for node in route]
    return route_coords


def calculaRotaOtima(G_Direcional, nos_origem, no_destino, raio=0.500):

    def handletimeout(signum, frame):
        raise TimeoutError

    signal.signal(signal.SIGALRM, handletimeout)

    rotas_otimas = []
    linhas_otimas = []

    for no_origem in nos_origem:

        try:
            signal.alarm(SECONDS)
            # paradas, linhas_usadas = dijkstra(G_Direcional, no_origem, no_destino, raio)
            paradas, _ = dijkstra(G_Direcional, no_origem, no_destino, raio)

            linhas_usadas = calculaLinhasOnibusUsadas(G_Direcional, paradas)

            rotas_otimas.append(paradas)
            linhas_otimas.append(linhas_usadas)
        except TimeoutError:
            paradas, linhas_usadas = [], MAX_LINHAS
            rotas_otimas.append(paradas)
            linhas_otimas.append(linhas_usadas)
        finally:
            signal.alarm(RESET)

    todasLinhas = []
    for rota in linhas_otimas:
        linhas = []
        if len(rota) == LEN_MAX_LINHAS:
            todasLinhas.append(rota)
            continue

        for linha in rota[1:]:
            if linha not in linhas:
                linhas.append(linha)
        todasLinhas.append(linhas)

    indice = min(range(len(todasLinhas)), key=lambda i: len(todasLinhas[i]))



    return rotas_otimas[indice], linhas_otimas[indice]


def dijkstra(grafo, origem, destino, raio=0.500):
    global minHeap

    distancias = {node: float('inf') for node in grafo.nodes}
    distancias[origem] = 0 
    predecessores = {}
    linhas = {}

    # Fila prioridade com: Distancia até o nó destino, Linha de Ônibus Atual, Nó atual
    heapq.heappush(minHeap, (0, None, origem))

    while minHeap:

        distancia_atual, linha_atual, no_atual = heapq.heappop(minHeap)

        if no_atual == destino or (calculaDistanciaEntreNos(grafo, no_atual, destino) <= raio):
            caminho = []
            linhas_caminho = []
            while no_atual is not None:
                caminho.append(no_atual)
                linhas_caminho.append(linhas.get(no_atual))
                no_atual = predecessores.get(no_atual)
            return list(reversed(caminho)), list(reversed(linhas_caminho))

        if distancia_atual > distancias[no_atual]:
            continue

        for vizinho in grafo.neighbors(no_atual):

            linha_atual_aux = linha_atual
            dist_atual_aux = distancia_atual
            arestas = grafo.get_edge_data(no_atual, vizinho)

            if calculaDistanciaEntreNos(grafo, no_atual, vizinho) <= RAIO_PARADAS_PROXIMAS: 
                distancias[vizinho] = dist_atual_aux
                linhas[vizinho] = linha_atual_aux
                predecessores[vizinho] = no_atual
                heapq.heappush(minHeap, (dist_atual_aux, linha_atual_aux, vizinho))
                continue
            
            if linha_atual_aux is None:
                dist_atual_aux += arestas['dist']
                linha_atual_aux = arestas['linha'][IDX_PRIMEIRA_LINHA]
            elif linha_atual_aux in arestas['linha']:
                dist_atual_aux += arestas['dist']
            else:
                dist_atual_aux += PESO * arestas['dist']
                linha_atual_aux = arestas['linha'][IDX_PRIMEIRA_LINHA]
        
            if distancia_atual < distancias[vizinho]:
                distancias[vizinho] = dist_atual_aux
                linhas[vizinho] = linha_atual_aux
                predecessores[vizinho] = no_atual
                heapq.heappush(minHeap, (dist_atual_aux, linha_atual_aux, vizinho))

    return [], []


# Função para calcular a distância euclidiana entre dois pontos
def calculaDistanciaEntreNos(grafo, no_origem, no_destino):
    origem = (grafo.nodes[no_origem]['coords'].y, grafo.nodes[no_origem]['coords'].x)
    destino = (grafo.nodes[no_destino]['coords'].y, grafo.nodes[no_destino]['coords'].x)
    return geodesic(origem, destino).km


def calculaRotaOtimaNx(G, nos_origem, nos_destino):

    def handletimeout():
        raise TimeoutError

    rotas_otimas = []
    linhas_otimas = []

    signal.signal(signal.SIGALRM, handletimeout)

    for no_origem in nos_origem:
        for no_destino in nos_destino:
            try:
                signal.alarm(5)
                
                paradas = nx.shortest_path(G, no_origem, no_destino, weight='dist', method='dijkstra')
                linhas_usadas = calculaLinhasOnibusUsadas(G, paradas)

                rotas_otimas.append(paradas)
                linhas_otimas.append(linhas_usadas)
            except TimeoutError:
                paradas, linhas_usadas = [], MAX_LINHAS
                rotas_otimas.append(paradas)
                linhas_otimas.append(linhas_usadas)
            finally:
                signal.alarm(0)

    indiceLinhaMenorQtdOnibus = None
    menorQtdOnibus = 50

    for idx, rota in enumerate(linhas_otimas):
        linhas = []
        qtdOnibus = 0

        for linha in rota[1:]:
            if linha not in linhas:
                qtdOnibus += 1
                linhas.append(linha)

        if qtdOnibus < menorQtdOnibus:
            menorQtdOnibus = qtdOnibus
            indiceLinhaMenorQtdOnibus = idx

    indice = indiceLinhaMenorQtdOnibus

    return rotas_otimas[indice], linhas_otimas[indice]


def calculaLinhasOnibusUsadas(G, paradas):

    linhas = []

    for i in range(1, len(paradas)):
        orig = paradas[i-1]
        dest = paradas[i]
        linha_orig_dest = G[orig][dest].get('linha')
        linhas.append(linha_orig_dest)

    return encontrarLinhasOtimas(linhas)


def encontrarLinhasOtimas(todasLinhas):

    idx_atual = 0
    linhasOtima_list = [None]

    while ( idx_atual < len(todasLinhas) ):
        idx_atual, linhas_longe = encontraLinhaMaisLonge(todasLinhas, idx_atual)
        linhasOtima_list.extend(linhas_longe)
        
    return linhasOtima_list


def encontraLinhaMaisLonge(todasLinhas, idx_atual):

    indice_max = idx_atual
    linha_max = todasLinhas[idx_atual][0]

    for _, linha_y in enumerate(todasLinhas[idx_atual]):
        prox_idx = idx_atual + 1
        while prox_idx < len(todasLinhas):
            if linha_y in todasLinhas[prox_idx]:
                if prox_idx > indice_max:
                    indice_max = prox_idx
                    linha_max = linha_y
            prox_idx += 1

    repeticoes = (indice_max + 1) - idx_atual
    idx_atual += repeticoes

    linhasOtima_list = [linha_max] * repeticoes

    return idx_atual, linhasOtima_list


def paradasELinhasToJson(G, paradas, linhas_usadas):
    paradas_info = []
    linhas_usadas = linhas_usadas[1:]

    parada_info = {
        "id_stop": int(paradas[0]),
        "lat": float(G.nodes[paradas[0]]['coords'].y),
        "lon": float(G.nodes[paradas[0]]['coords'].x),
    }
    paradas_info.append(parada_info)

    # Itera sobre as paradas e linhas para criar o dicionário
    for i, parada in enumerate(paradas[1:]):
        parada_info = {
            "id_stop": int(parada),
            "lat": float(G.nodes[parada]['coords'].y),
            "lon": float(G.nodes[parada]['coords'].x),
            "linha": str(linhas_usadas[i])
        }
        paradas_info.append(parada_info)
    
    return paradas_info