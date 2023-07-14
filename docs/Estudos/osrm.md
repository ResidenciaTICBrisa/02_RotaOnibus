# OSRM

## Introdução

O Open Source Routing Machine (OSRM) é um motor de encaminhamento de alto desempenho para encontrar os caminhos mais curtos em redes rodoviárias. Escrito em C++ e foi concebido para funcionar com os dados abertos e gratuitos da rede rodoviária do projeto OpenStreetMap (OSM). O OSRM combina algoritmos de encaminhamento sofisticados com dados do OSM para calcular e produzir rapidamente o caminho mais curto entre qualquer origem e destino em poucos milissegundos.

### OSRM C++ é o mesmo que o OSRM Python?

- Não, o OSRM não é uma biblioteca Python abstraída da implementação C++. - O OSRM (Open Source Routing Machine) é principalmente um motor de encaminhamento C++ para encontrar os caminhos mais curtos em redes rodoviárias. Foi concebido para trabalhar com dados do OpenStreetMap (OSM) e fornece cálculos de encaminhamento rápidos.

- No entanto, existe uma biblioteca Python chamada osrm que permite interagir com o motor de encaminhamento OSRM utilizando Python. Esta biblioteca fornece uma forma conveniente de fazer consultas de encaminhamento, calcular distâncias e obter direcções entre locais utilizando o backend OSRM.

- Assim, enquanto o próprio OSRM é implementado em C++, a biblioteca osrm Python funciona como um invólucro ou interface para interagir com o motor de encaminhamento OSRM num ambiente Python.

### Compreendendo os princípios básicos do OSRM

- O OSRM é uma implementação em C++ de um mecanismo de roteamento para caminhos mais curtos em redes rodoviárias.
- Está licenciado sob a licença permissiva BSD de 2 cláusulas e é um serviço de rede gratuito.
- O OSRM suporta as plataformas Linux, FreeBSD, Windows e Mac OS X.

### Recursos do OSRM

- O OSRM permite aos utilizadores criar perfis personalizáveis, que definem a forma como o motor de encaminhamento trata os diferentes tipos de estradas.
- Suporta vários modos de transporte, como a condução, o ciclismo, a marcha e o encaminhamento de cadeiras de rodas.
- O OSRM pode ser configurado num servidor para fornecer serviços de encaminhamento para aplicações.
- Os utilizadores podem consultar os dados de encaminhamento utilizando a API do OSRM.

### Instalação do OSRM

- É possível instalar o OSRM no Ubuntu 20.04 seguindo as instruções fornecidas em [LinuxBabe](https://www.linuxbabe.com/ubuntu/install-osrm-ubuntu-20-04-open-source-routing-machine).
- O OSRM fornece imagens Docker que facilitam a configuração do seu próprio mecanismo de roteamento.

### Explore o OSRM com Python

- O OSRM pode ser facilmente interagido usando Python.
- Depois de configurar o backend do OSRM, pode utilizar Python para fazer consultas de encaminhamento e calcular distâncias e direcções entre locais.

## Implementação de rotas de onibus

- Compreender as limitações do OSRM relativamente ao encaminhamento de trânsito. O OSRM não suporta nativamente o roteamento de trânsito. Foi concebido principalmente para o encaminhamento ao nível da rua para carros, bicicletas. No entanto, existem soluções alternativas para permitir o encaminhamento de ônibus usando o OSRM.

- Copie o perfil car.lua e crie um novo perfil chamado onibus.lua. Os perfis no OSRM determinam as listas brancas/negras para tipos de estrada, superfícies de estrada e obstáculos de manuseamento. Ao criar um novo perfil, pode personalizar o comportamento de encaminhamento para percursos de onibus.

- Adapte o perfil onibus.lua para definir velocidades específicas para determinados tipos de superfície relevantes para o encaminhamento de autocarros. Esta personalização permite-lhe simular melhor os tempos de viagem dos onibus em diferentes superfícies rodoviárias.

- Utilize o OpenStreetMap (OSM) para mapear as rotas de autocarro utilizando relações. As rotas de autocarro no OSM são normalmente mapeadas utilizando relações. Historicamente, o OSRM não suportava relações de rotas, o que tornava difícil o mapeamento de onibus. No entanto, o suporte para relações de rotas foi adicionado ao OSRM em versões recentes.

- O OSM não contém informações sobre horários para rotas de onibus. Por conseguinte, quaisquer itinerários de onibus gerados com o OSRM serão teóricos e poderão não refletir os horários reais dos onibus. Para obter itinerários de onibus mais precisos e realistas, tendo em conta os horários, poderá querer explorar outros motores de itinerários, como o Graphhopper ou o OpenTripPlanner.

## Implementação utilizando o OSRM para calcular a rota mais rápida entre duas cordenadas

```python
import osrm

# Initialize OSRM engine
engine_config = osrm.EngineConfig(storage_config="path/to/osrm/files")
osrm_instance = osrm.OSRM(engine_config)

# Define the coordinates for the start and end points
start_coord = osrm.Coordinate(13.388860, 52.517037)  # latitude, longitude
end_coord = osrm.Coordinate(13.397634, 52.529407)

# Create the route parameters
route_params = osrm.RouteParameters()
route_params.coordinates.extend([start_coord, end_coord])

# Call the Route function to calculate the route
result = osrm_instance.Route(route_params)

# Extract the distance and duration from the result
distance = result.routes[0].distance
duration = result.routes[0].duration

print(f"The distance is {distance} meters and the duration is {duration} seconds.")
```

## Histórico de Versão

| Versão |          Alteração           | Responsável  | Revisor | Data  |
| :----: | :--------------------------: | :----------: | :-----: | :---: |
|  1.0   | Criando documentação do OSRM | Lucas Frazão |    -    | 14/07 |
