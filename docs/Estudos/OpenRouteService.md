# OpenRouteService (ORS)

## 1. Introdução

O OpenRouteService (ORS) é um serviço de roteamento de código aberto que foi desenvolvido pela primeira vez em 2008 pela Universidade de Heidelberg, na Alemanha. O projeto foi iniciado pelo Departamento de Geografia e pelo Instituto Interdisciplinar de Estudos Cognitivos Avançados (IKI) da universidade.

O OpenRouteService foi desenvolvido com o objetivo de fornecer soluções de roteamento e planejamento de rotas eficientes, acessíveis e personalizáveis para uma variedade de aplicações.
    

## 2. Informações Relevantes

As principais informações sobre o ORS podem ser vistas na seguinte listagem:

1. **Roteamento avançado**: O OpenRouteService permite calcular rotas otimizadas para diferentes tipos de modos de transporte, como carro, bicicleta e a pé. Ele leva em consideração as características específicas de cada modo, como restrições de velocidade, preferências de estrada e restrições de acesso.

2. **Geocodificação**: A plataforma fornece serviços de geocodificação, permitindo converter endereços em coordenadas geográficas (latitude e longitude) e vice-versa. Isso permite que você localize e identifique pontos específicos no mapa com base em informações de endereço.

3. **Isocróna**: A funcionalidade de isócrona permite visualizar áreas alcançáveis em um determinado tempo de viagem a partir de um local ou uma série de locais. Isso é útil para determinar a área que pode ser alcançada em um determinado período de tempo, seja a pé, de bicicleta ou de carro.

4. **Serviço de matriz de distância**: O OpenRouteService pode calcular uma matriz de distância que fornece a distância entre múltiplos pontos de origem e destino. Essa funcionalidade é útil para encontrar a distância mais curta entre vários pontos ou calcular a distância total de um percurso com várias paradas.

5. **Dados Abertos**: O OpenRouteService é baseado na plataforma de mapeamento colaborativo OpenStreetMap, que é alimentada por dados abertos e contribuições da comunidade. Isso significa que os usuários podem contribuir para melhorar a qualidade dos dados do mapa, bem como acessar e utilizar os dados de forma gratuita.

6. **Integração flexível**: A plataforma oferece uma [API](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/blob/main/docs/Estudos/Django.md#31-api) que permite a integração em diferentes aplicativos e serviços. Isso significa que desenvolvedores podem usar as funcionalidades do OpenRouteService em seus próprios aplicativos ou serviços para fornecer recursos de roteamento e geolocalização.

## 3. Cálculo de melhor rota entre dois pontos
 
O ORS possui diversos métodos usados para os cálculos das rotas, entre os mais importante está o método GET Directions que é usado para obter a melhor rota entre dois pontos. Ele fornece informações detalhadas sobre as direções de viagem, incluindo instruções passo a passo, distância, duração estimada, coordenadas geográficas dos pontos de virada, entre outros.

Para chamar o método é necessário fazer uma solicitação HTTP GET para o endpoint apropriado, fornecendo os parâmetros necessários. 
    
    GET /v2/directions/{profile}/{coordinates}

{profile} representa o modo de transporte desejado, como carros, bicicletas, pedestres, etc.
{coordinates} é uma lista de coordenadas geográficas dos pontos de partida e chegada, bem como quaisquer pontos intermediários que você deseja incluir na rota.

Também é possível fornecer outros parâmetros opcionais, como restrições de rota, preferências de estrada, evitando pedágios ou rodovias e etc.

A resposta da solicitação fornecerá informações detalhadas sobre a rota, incluindo o resumo da rota, uma matriz de coordenadas geográficas ao longo da rota, instruções passo a passo e outras informações úteis.

### Exemplo

O Link [Exemplo de cálculo de rota](https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce3597851110001cf6248db9786ac4c7446dea93a21d0c244d5b2&start=8.681495,49.41461&end=8.687872,49.420318) serve como exemplo do funcionamento da API.

Onde o meio de transporte escolhido é um carro e as coordenadas são 8.681405, 49.41461 para o ponto de partida e 8.687872, 49.420318 para o ponto de chegada.

Com isso é possível obter um JSON que contém dados de toda rota como: a distância total, o tempo total, a distancia e o tempo entre cada um dos pontos, além de instruções de como seguir de um ponto até outro.

## 4. Referências

- [1] [OpenRouteService GitHub](https://github.com/GIScience/openrouteservice)
- [2] [API Playground](https://openrouteservice.org/dev/#/api-docs)

## 5. Histórico de Versão

| Versão |          Alteração           | Responsável | Revisor | Data  |
| :----: | :--------------------------: | :---------: | :-----: | :---: |
|  1.0   | Criando documentação do ORS  | João Leles  |    -    | 13/07 |
|  1.1   |     Adicionando Exemplo      | João Leles  |    -    | 14/07 |