# Construção da Rota Ótima

## 1. Notebook 

O notebook para a Construção do Grafo que utilizamos para encontrar a melhor rota em que o usuário irá pegar para o seu destino final, encontra-se no link a seguir:

- [Notebook para rota ótima](/docs/Notebooks/PreProcessamento/RotaOtima-Grafo.ipynb)

## 2. Lendo o grafo estático
lendo o Grafo  salvado estaticamente que foi gerado para carregar e usar quando necessário.

        # Ler o grafo de um arquivo usando pickle
        with open('grafoDirecional.grafo', 'rb') as f:
            G = pickle.load(f)

## 3. Encontrar as paradas mais próximos em um raio de distância

Para começar a traçar a melhor rota que um usuário final irá utilizar para chegar ao seu destino final, o primeiro passo é encontrar a parada inicial, para isso precisa-se encontrar as paradas mais próximas a partir do ponto onde o usuário está, para que possa fazer a baldeação entre o usuário e a parada inicial. Para isso utilizamos um raio em metros para encontrar as paradas mais próximas, com uma distancia que o usuário final consiga andar até a parada. O código resultante é o apresentado a seguir:

        raio = 0.007  # Raio desejado em metros ???

        origem = (-15.989444964529529, -48.044418962814866) # Unb Gama
        destino = (-15.917416518011471, -48.04883853393932)   # Conjunto Nacional

        destino2 = (-15.917416518011471, -48.04883853393932) # parada recanto br
        #destino2 = (-15.903808679809567, -48.06531532666961)

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


        def calculaNosProximos(G, long, lat, raio):
            nos_proximos = []
            ponto = Point(long, lat)
            for node in G.nodes():
                node_coords = Point(G.nodes[node]['coords'])
                dist = node_coords.distance(ponto)
                if dist <= raio:
            nos_proximos.append(node)
            return nos_proximos

        nos_origem = calculaNosProximos(G, origem[1], origem[0], raio)
        no_destino = calculaNoProximo(G, destino2[1], destino2[0])

        # Mapa folium
        m = folium.Map(location=[origem[0], origem[1]], zoom_start=14)

        #Marcadores para os nós próximos de origem
        for node in nos_origem:
            coords = G.nodes[node]['coords']
            folium.Marker([coords.y, coords.x], icon=folium.Icon(color='blue')).add_to(m)

        # Marcadores para os nós próximos de destino
        coords = G.nodes[no_destino]['coords']
        folium.Marker([coords.y, coords.x], icon=folium.Icon(color='red')).add_to(m)

        # Exiba o mapa
        m

## 4. Algoritmo rota ótima

- Deve receber o nó origem e o nó destino do Grafo
- Percorrer o Grafo usando algoritmo de Dijkstra, cujo o peso é a distancia entre as arestas
- Armazenar as Paradas percorridas e as linhas de ônibus necessárias para chegar da origem ao destino

Esse algoritmo encontra todos os pontos (paradas) que compoem a rota.

        # Calcula rota otima com algoritmo de Dijkstra
        rota_otima = nx.shortest_path(G, nos_origem[4], no_destino, weight="dist", method="dijkstra")

        print(rota_otima)


## 5. Utilizando Dijkstra para adicionar peso nas baldeações

O algoritmo de Dijkstra é um algoritmo de busca em grafos usado para encontrar o caminho mais curto entre um nó de origem e todos os outros nós em um grafo ponderado, com pesos não negativos nas arestas. Ele mantém uma lista de distâncias mínimas conhecidas a partir da origem e gradualmente expande essas distâncias à medida que explora o grafo, escolhendo sempre o nó não visitado mais próximo da origem. O algoritmo é eficiente para grafos densos, mas pode não ser adequado para grafos com pesos negativos ou ciclos. O resultado final é um conjunto de distâncias mínimas e os caminhos associados a partir da origem para todos os outros nós no grafo. Utilizamos esse algoritmo para colocar um peso para que o algoritmo trace uma rota com menos onibus possíveis.

- Caso o algoritmo troque de linha de onibus (altere de um nó que seguia uma linha de onibus X, para um nó que segue linha de ônibus Y)
- Então a distância entre os nós deve ser multiplicada por um fator *K*, para dificultar a baldeação de linhas

        raio = 0.500

        linhas_otimas = []

        for no_origem in nos_origem:
            rota_otima, linha_otima = dijkstra(G, nos_origem[4], no_destino, raio)
            if linha_otima is not None:
                linhas_otimas.append(linha_otima)
            else:
                linhas_otimas.append("Nenhuma linha de ônibus encontrada para o destino")

