# Benchmark do OpenRouteService

## 1. Introdução

Benchmark da API do OpenRouteService, buscando traçar uma rota entre dois pontos (FGA e Conjunto Nacional) com o objetivo de avaliar a complexidade e a dificuldade em utilizar a ferramenta, bem como medir o seu tempo de resposta.

## 2. Visualizando as rotas

### 2.1 Bibliotecas

As seguintes bibliotecas foram usadas para avaliar a API:

    import openrouteservice as ors
    import folium
    import math

### 2.2 Chave da API

O ORS necessita de uma chave de ativação para poder traçar uma rota, ela pode ser obtida neste site [ORS Docs](https://openrouteservice.org/dev/#/api-docs) e utilizada como no codigo a seguir:

    client = ors.Client(key='YOUR_KEY')

### 2.3 Menor Rota Entre Dois Pontos

Utilizando a biblioteca openrouteservice é possível calcular a rota entre dois pontos, nesse caso, a rota entre a FGA e o Conjunto Nacional.

    # Coordenadas da rota
    coordenadas = [[-48.045285,-15.989108], [-47.882799,-15.791886]]

    # Define o perfil da rota
    rota = client.directions(coordinates = coordenadas, profile = 'driving-car', format = 'geojson')

    # Traça a rota no mapa
    folium.PolyLine(locations=[list(reversed(coord)) for coord in rota['features'][0]['geometry']['coordinates']], color='blue').add_to(mapa)

### 2.4 Otimização de rotas 

A API do OpenRouteService apresentou recursos avançados de otimização de rotas ao dividir as coordenadas em mais de um veículo. Foi possível marcar um local de início (rodoviária) e criar rotas para três veículos distintos. Funcionalidade essa que também pode ser usada no transporte público.
    
    # Marca o local de inicio
    rodoviaria = [-47.8833709,-15.7934468]
    mapa = folium.Map(location=list(reversed([-47.885729,-15.798224])), tiles="cartodbpositron", zoom_start = 13)
    folium.Marker(location=list(reversed(rodoviaria)), icon=folium.Icon(color="red")).add_to(mapa)

    # Divide as coordenadas e cria rotas para três veiculos
    coords = [
    [-47.894583,-15.810909],
    [-47.962913,-15.896979],
    [-47.990700,-15.945459],
    [-48.047356,-15.989687],
    [-47.874270,-15.775838],
    [-47.866248,-15.770699],
    [-47.869608,-15.757577],
    [-47.876013,-15.753971],
    [-47.890927,-15.795877],
    [-47.926040,-15.759948],
    [-47.932124,-15.788361],
    ]

    vehicles = [
    ors.optimization.Vehicle(id=0, profile='driving-car', start=rodoviaria, end=rodoviaria, capacity=[4]),
    ors.optimization.Vehicle(id=1, profile='driving-car', start=rodoviaria, end=rodoviaria, capacity=[4]),
    ors.optimization.Vehicle(id=2, profile='driving-car', start=rodoviaria, end=rodoviaria, capacity=[3]),
    ]

    jobs = [ors.optimization.Job(id=index, location=coords, amount=[1]) for index, coords in    enumerate(coords)]
    optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
    line_colors = ['green', 'blue', 'yellow']
    for route in optimized['routes']:
    folium.PolyLine(locations=[list(reversed(coords)) for coords in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_colors[route['vehicle']]).add_to(mapa)

### 2.5 Tempo de Rota

No caso anterior também é possível adicionar um tempo para cada uma das rotas assim como um tempo de serviço de cada um dos veículos
    
    # Organiza a rota de acordo com o tempo
    coords = [ 
        { 'location': [-47.894583,-15.810909],'service': 1*60*60 },
        { 'location': [-47.962913,-15.896979],'service': 0.5*60*60 },
        { 'location': [-47.990700,-15.945459],'service': 0.75*60*60 },
        { 'location': [-48.047356,-15.989687],'service': 1*60*60 },
        { 'location': [-47.874270,-15.775838],'service': 0.25*60*60 },
        { 'location': [-47.866248,-15.770699],'service': 0.3*60*60 },
        { 'location': [-47.869608,-15.757577],'service': 0.2*60*60 },
        { 'location': [-47.876013,-15.753971],'service': 0.1*60*60 },
    ]

    rodoviaria = [-47.8833709,-15.7934468]
    mapa = folium.Map(location=list(reversed([-47.885729,-15.798224])), tiles="cartodbpositron", zoom_start = 13)
    folium.Marker(location=list(reversed(rodoviaria)), icon=folium.Icon(color="red")).add_to(mapa)

    vehicles = [
    ors.optimization.Vehicle(id=0, profile='driving-car', start=rodoviaria, end=rodoviaria, time_window=[0, 2*60*60]),
    ors.optimization.Vehicle(id=1, profile='driving-car', start=rodoviaria, end=rodoviaria, time_window=[0, 4*60*60])
    ]
    jobs = [ors.optimization.Job(id=index, **job) for index, job in enumerate(coords)]
    optimized = client.optimization(jobs=jobs, vehicles=vehicles, geometry=True)
    line_colors = ['green', 'orange', 'blue', 'yellow']
    for route in optimized['routes']:
    folium.PolyLine(locations=[list(reversed(coords)) for coords in ors.convert.decode_polyline(route['geometry'])['coordinates']], color=line_colors[route['vehicle']]).add_to(mapa)
    for step in route['steps']:
        if not step['type'] == 'job':
            continue
        folium.Marker(location=list(reversed(step['location'])), popup=f"Arrival time: {math.floor(step['arrival'] / (60*60))} hours {math.floor((step['arrival'] % (60*60)) / 60)} minutes", icon=folium.Icon(color=line_colors[route['vehicle']])).add_to(mapa)

## 3. Conclusão

Em conclusão, a API do OpenRouteService mostrou-se uma ferramenta poderosa para cálculo e otimização de rotas geográficas. Através do uso da biblioteca openrouteservice, é possível facilmente obter rotas entre pontos específicos e, com o recurso de otimização, distribuir tarefas entre múltiplos veículos de forma eficiente. Isso torna a API adequada para uma ampla gama de aplicações, desde navegação veicular até logística e planejamento de rotas para empresas de ônibus.

## 4. Referências

- [Getting Directions in Python with OpenRouteService-py](https://syntaxbytetutorials.com/vehicle-route-optimization-in-python-with-openrouteservice/)
- [VROOM GitHub](https://github.com/VROOM-Project/vroom/blob/master/docs/API.md)

## 5. Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criando documentação do Benchmark do ORS | João Leles | - | 17/07 |