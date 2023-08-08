# Rotas em Grafos (Pseudocódigo)

## Tratamento das Paradas e Rotas de ônibus do DF 
 
A [Semob](https://semob.df.gov.br/) (Secrataria de Transporte e Mobilidade) do Distrito Federal fornece todos os dados sobre as paradas e rotas de ônibus em arquivos de vários formatos nesse [link](https://geoserver.semob.df.gov.br/geoserver/web/wicket/bookmarkable/org.geoserver.web.demo.MapPreviewPage?0&filter=false). Mas o formato que mais interessa para o contexto do projeto é o arquivo [Shapefile](https://residenciaticbrisa.github.io/02_RotaOnibus/#/./Estudos/EstudoShapeFiles?id=_1-o-que-s%c3%a3o-arquivos-shapefiles) das paradas e ônibus. 

O arquivo Shapefile das paradas, após ser lido e transformado em um GeoDataFrame, é descrito com as informações apresentadas na Figura 1. A coluna 'geometry' contém o POINT das paradas, ou seja, o GPS (latitude e longitude) delas. Essa coluna será importante pois iremos tentar encontrar essas coordenadas das paradas nas linhas de ônibus.

![DataFrame Paradas](./assets/dataFrameParadas.png)
<p align="center">Figura 1. DataFrame Paradas</p>

Já o arquivo Shapefile das linhas, após ser lido e transformado em um GeoDataFrame, é descrito com as informações apresentadas na Figura 2. A coluna 'geometry' agora contém uma LINESTRING da linha de ônibus, ou seja, todos os pontos que uma ônibus passa até completar a rota completa. Dessa maneira, esse LINESTRING de cada rota possuí informações irrelevantes (todo o trajeto feito pelo ônibus) para o usuário final. Sendo assim, o objetivo dessa limpeza é retirar todos os pontos desnecessários da LINESTRING de cada rota, resultando em uma LINESTRING que possua apenas os POINTs das paradas de ônibus por qual uma rota trafega.

![DataFrame Linhas](./assets/dataFrameLinhas.png)
<p align="center">Figura 2. DataFrame Linhas</p>

Todo o tratamento das paradas e linhas de ônibus pode ser encontrada nesse [notebook](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/blob/main/docs/Notebooks/testeParadas.ipynb).

Em resumo, o [notebook](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/blob/main/docs/Notebooks/testeParadas.ipynb) trabalha com dados de uma linha específica e pontos de parada de ônibus. O scrip principal tem como objetivo, iterar sobre os POINTS de parada de ônibus presentes no shapefile das paradas, calculando a distância entre cada ponto e a linestring de uma linha de ônibus. Se a distância for menor do que um valor específico, o ponto de parada é considerado próximo o suficiente e é registrado. Um novo conjunto de dados é criado com os pontos de parada próximos identificados.

Usando a biblioteca de mapeamento folium, o código cria um mapa interativo e adiciona marcadores para cada ponto de parada próximo. Cada marcador exibe informações sobre a parada quando clicado. Por fim, o mapa é salvo como um arquivo HTML.

## Estrutura do Grafo

Após essa primeira etapa de tratamento dos dados, foi gerado um arquivo CSV que contém todas as paradas de uma linha de ônibus. Então, com esse Data Frame em mãos, foi pensado na construção do Grafo com o Pseudocódigo a seguir:


        Para cada linha (rota) no DataFrame:
            Criar um novo Grafo Direcional chamado subgrafo
        
            Para cada parada na linha:
                Adicionar um nó ao subgrafo para representar a parada
                Armazenar o identificador e coordenada da parada
                
            Para cada parada de 1 até o penúltimo nó:
                Calcular a distância entre a parada atual e a próxima parada
                Adicionar uma aresta do nó atual para o próximo nó com a distância e o número da linha de ônibus como atributos
                
            Calcular a distância entre a última parada e a primeira parada
            Adicionar uma aresta do último nó para o primeiro nó com a distância como atributo
            
            Adicionar o subgrafo ao grafo principal


Dessa forma, os nós e arestas do Grafo estariam descritos dessa forma a seguir:

- Nó : identificador da parada de ônibus, coordenada da parada de ônibus
- Aresta: número da linha de ônibus e a distancia entre os nós


## Replicar para todo o Brasil

O objetivo final seria então, replicar as etapas de tratamento das Paradas e Rotas de ônibus, bem como a contrução do Grafo para todos os estados do Brasil. De tal forma que a última etapa consiste em juntar todos os Grafos de cada estado em apenas um único. A partir disso, a fase de transformar os notebooks em uma API Restful pode ser inicializada.


## Referências

- 1. [Semob](https://semob.df.gov.br/)

## Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criação Pseudocódigo  | Leonardo Vitoriano | - | 03/08 |



