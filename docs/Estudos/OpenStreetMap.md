# OpenStreetMap (OSM)

## 1. Introdução

O OpenStreetMap (OSM) é um projeto colaborativo e disponível gratuitamente que visa criar um mapa detalhado e editável do mundo. Foi lançado em 2004 e desde então se transformou em uma iniciativa ampla impulsionada pela comunidade, com contribuições de pessoas ao redor do globo. 

## 2. Aspectos Relevantes

As principais características o OpenStreetMap podem ser encontradas na listagem a seguir:

1. **Coleta de Dados**: O OpenStreetMap conta com uma grande comunidade de voluntários que contribuem com dados geográficos, mapeando diferentes elementos, como estradas, edifícios, pontos de referência, rios e pontos de interesse. Os colaboradores utilizam dispositivos GPS, imagens de satélite, fotografias aéreas e conhecimento local para coletar e digitalizar os dados do mapa.

2. **Elementos Geográficos**: Os dados do mapa no OpenStreetMap são representados por três elementos fundamentais:
    - **Nós**: Representam pontos individuais no mapa com coordenadas de latitude e longitude. Os nós são usados para marcar locais específicos, como postes de iluminação ou entradas de lojas.
    - **Vias**: As vias são sequências de nós conectados, representando elementos lineares, como estradas, rios ou caminhos. As vias podem ter atributos, como classificação de estrada (por exemplo, rodovia, residencial) ou tipo (por exemplo, pedestres, ciclovia).
    - **Relações**: As relações definem relações geométricas ou lógicas complexas entre vários elementos. Por exemplo, uma relação pode agrupar várias vias para definir uma fronteira ou uma rota.

3. **Tags**: O OpenStreetMap utiliza um sistema de marcação (tags) para fornecer informações adicionais sobre os elementos mapeados. As tags consistem em pares de chave-valor e são usadas para descrever atributos e propriedades de nós, vias e relações. Por exemplo, uma estrada pode ter tags indicando seu nome, número de faixas, limites de velocidade e tipo de pavimento.

4. **Edição de Dados**: O OpenStreetMap oferece um editor baseado na web chamado iD, que permite que os usuários contribuam facilmente para o mapa adicionando, modificando ou excluindo elementos do mapa. Além disso, usuários mais avançados podem optar por editar os dados do mapa usando softwares como o JOSM (Java OpenStreetMap Editor).

5. **Dados Abertos**: Um dos princípios fundamentais do OpenStreetMap é que os dados do mapa são abertos e disponíveis gratuitamente para todos. Os dados são licenciados sob a Licença de Banco de Dados Aberta (ODbL), que permite que os usuários acessem, usem e distribuam os dados, desde que quaisquer trabalhos derivados sejam compartilhados sob a mesma licença.

6. **Qualidade e Verificação dos Dados**: O OpenStreetMap emprega um modelo impulsionado pela comunidade para garantir a qualidade dos dados. Os dados são continuamente revisados, validados e aprimorados pela comunidade de colaboradores. Os usuários também podem participar de discussões, relatar erros e sugerir melhorias por meio de diversos canais de comunicação dentro da comunidade.

7. **API e Desenvolvimento**: O OpenStreetMap disponibiliza uma API que permite que os desenvolvedores acessem, consultem e contribuam com os dados do mapa programaticamente. A API oferece suporte a diversas operações, incluindo recuperação de dados do mapa, geocodificação de endereços, cálculo de rotas e realização de consultas complexas usando a API Overpass.

8. **Renderização de Mapas**: Os dados do OpenStreetMap podem ser renderizados em mapas visualmente atraentes usando diferentes motores de renderização. Esses motores processam os dados brutos do mapa e geram imagens ou blocos de mapa que podem ser exibidos em sites ou aplicativos de mapeamento. Os estilos dos mapas podem ser personalizados para atender a necessidades específicas, e os usuários podem escolher entre várias opções de renderização.

9. **Comunidade Internacional**: O OpenStreetMap possui uma comunidade diversa e vibrante de colaboradores em todo o mundo. O projeto tem sido fundamental no mapeamento de áreas que antes eram negligenciadas ou não possuíam mapas detalhados, especialmente em regiões onde os dados de mapeamento comercial são limitados ou caros.

O OpenStreetMap encontrou aplicações em diversos domínios, incluindo sistemas de navegação, serviços de roteamento, planejamento urbano, resposta a desastres, projetos humanitários, pesquisa e iniciativas de mapeamento comunitário. Sua natureza aberta e o esforço coletivo da comunidade o tornaram um recurso valioso e amplamente utilizado para dados geográficos.

## 3. Implementação utilizando o OSM para calcular a rota mais rápida entre duas cordenadas

Antes de tudo, é necessário conhecer as bibliotecas Python **osmnx** e **networkx** que são necessárias para trabalhar com dados OSM e realizar cálculos de roteamento.

### 3.1 Biblioteca osmnx 

O osmnx é uma biblioteca Python que simplifica o acesso, a manipulação e a análise de dados do OpenStreetMap. Ele permite que você baixe dados do OSM, crie grafos de rede a partir desses dados e fornece várias funcionalidades para análise espacial.

Algumas das principais funcionalidades do osmnx são:

- Download de dados do OpenStreetMap para uma determinada área geográfica, incluindo informações sobre estradas, ciclovias, ruas, edifícios, entre outros.
- Criação de grafos de rede a partir dos dados do OSM, onde os nós representam pontos geográficos e as arestas representam as conexões entre esses pontos.
- Recuperação de informações sobre a rede, como distâncias, direções permitidas, velocidades máximas, tipos de estrada, entre outros.
- Visualização de mapas e grafos de rede com suporte para personalização de estilos e camadas.

O osmnx é uma biblioteca poderosa para explorar, analisar e visualizar dados do OSM de forma eficiente. Ele facilita a obtenção de dados geográficos e a criação de grafos para realizar tarefas de roteamento e análise de rede.

### 3.2 Biblioteca networkx

O networkx é uma biblioteca Python para análise de redes. Ela fornece estruturas de dados, algoritmos e ferramentas para trabalhar com redes complexas e grafos.

Algumas das principais funcionalidades do networkx são:
- Criação e manipulação de grafos direcionados e não direcionados.
- Algoritmos de roteamento, como o algoritmo de Dijkstra, para encontrar caminhos mais curtos entre nós em um grafo.
- Algoritmos de análise de redes, como centralidade, comunidades, detecção de ciclos, entre outros.
- Funções para visualização e desenho de grafos.

O networkx é amplamente utilizado em diferentes áreas, incluindo ciência de dados, ciências sociais, biologia, física e, no contexto do OpenStreetMap, é comumente utilizado para calcular rotas e realizar análises em grafos de redes de transporte.

No contexto do roteamento com dados do OpenStreetMap, a combinação do osmnx e networkx permite que você baixe os dados do OSM, crie grafos de rede a partir desses dados e, em seguida, utilize os algoritmos de roteamento do networkx para calcular a menor rota entre dois pontos no mapa.
### 3.3 Tutorial

1. Primeiro, instale as bibliotecas Python necessárias **osmnx** e **networkx**. Você pode instalá-los usando pip:

```
pip install osmnx networkx
```

2. Importe os módulos necessários em seu script Python:

```python
import osmnx as ox
import networkx as nx
```

3. Use a biblioteca osmnx para baixar os dados OSM para a área desejada. Por exemplo, para baixar os dados do OSM para uma caixa delimitadora que cobre o Brasil, você pode usar o seguinte código:

```python
# Define the bounding box coordinates
north, south, east, west = 5.2719, -33.7684, -34.729, -73.9855

# Download the OSM data
graph = ox.graph_from_bbox(north, south, east, west, network_type='all')

```
Isso fará o download dos dados do OSM e criará um objeto gráfico networkx.

4. Você pode visualizar os dados OSM baixados para verificar se cobrem a área desejada. Use o seguinte código para plotar o mapa:

```python
# Plot the OSM data
ox.plot_graph(ox.project_graph(graph))
```

5. Para calcular o caminho de carro mais curto entre dois pontos, você precisa extrair os nós do grafo e usar a biblioteca networkx para realizar os cálculos de roteamento. Por exemplo, para calcular o caminho mais curto do carro usando o algoritmo Dijkstra, você pode usar o seguinte código:

```python
# Specify the source and target points (latitude, longitude)
source_point = (-15.7801, -47.9292)
target_point = (-23.5505, -46.6333)

# Find the nearest network nodes to the source and target points
source_node = ox.distance.nearest_nodes(graph, source_point[1], source_point[0])
target_node = ox.distance.nearest_nodes(graph, target_point[1], target_point[0])

# Calculate the shortest car path
shortest_path = nx.shortest_path(graph, source_node, target_node, weight='length')

```

No código acima, source_point e target_point representam as coordenadas de latitude e longitude dos pontos de origem e destino, respectivamente. A função near_nodes localiza os nós da rede mais próximos dos pontos especificados, e a função shortest_path calcula o caminho mais curto entre os nós com base no comprimento das arestas (estradas).

6. Você pode visualizar o caminho de carro mais curto no mapa usando o seguinte código:

```python
# Plot the shortest car path on the map
ox.plot_graph_route(graph, shortest_path, route_linewidth=6, node_size=0, bgcolor='k')
```

Este código destacará o caminho de carro mais curto no mapa.


## 4. Referências

- [Osmnx Docs](https://osmnx.readthedocs.io/en/stable/user-reference.html)
- [OSM Main Page](https://wiki.openstreetmap.org/wiki/Main_Page)
- [Overpass API](https://wiki.openstreetmap.org/wiki/Overpass_API)
- [Networkx](https://networkx.org/documentation/stable/auto_examples/geospatial/plot_osmnx.html)
- [Osmnx Tutorial](https://geoffboeing.com/2016/11/osmnx-python-street-networks/)
- [routing-speed-time Tutorial](https://github.com/gboeing/osmnx-examples/blob/v0.13.0/notebooks/02-routing-speed-time.ipynb)

## 5. Histórico de Versão

| Versão | Alteração |  Responsável  | Revisor | Data  |
| ------ | :-------: | :-----------: | :-----: | :---: |
|  1.0   | Criando introdução e aspectos relevantes | Leonardo Vitoriano |  -  | 07/07/23 |
|  1.1   | Adicionando implementação com OSM | Leonardo Vitoriano |  -  | 14/07/23 |


