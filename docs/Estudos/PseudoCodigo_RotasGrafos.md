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

<!-- DECLARE grafoGeral {O grafo tem que ser Direcional} -->
<!-- DECLARE subGrafo -->

<!-- proxParada <- parada + 1 % tamanhoDF { Ca} -->

<!-- tamanhoLineString <- Quantidade de linhas do linestring -->

        LEIA(DataFrameRotas)
        DataFramaParadas <- CRIE DataFrame da coluna 'geometry' presente em DataFrameRotas
        grafoRotas <- CHAME método que cria Grafo Direcional vazio  

        PARA cada parada no DataFramaParadas FACA
            SE parada NÃO está no grafoRotas ENTÃO 
                CHAME método que adiciona a parada como um Nó do grafoRotas 
            FIM SE
        FIM PARA

            CHAME método que junta o grafoSubRota ao grafoRotas

<!-- LEIA(DataFrameRotas)
DataFramaParadas <- CRIE DataFrame da coluna 'geometry' presente em DataFrameRotas
grafoRotas <- CHAME método que cria Grafo Direcional vazio  

PARA cada linha no DataFrameRotas FAÇA

    linestring <- ACESSE paradas de uma rota de ônibus da linha
    grafoSubRota <- CHAME método que cria Grafo Direcional vazio

    PARA cada parada no linestring FACA
        CHAME método que adiciona a parada como um Nó do grafoSubRota 
    FIM PARA

    CHAME método que junta o grafoSubRota ao grafoRotas
    
FIM PARA -->



<!-- df <- Data Frame das paradas e linhas
Grafo <- Grafo direcional 

para cada linha no df: 
    linestring <- paradas de uma linha

    para cada parada no linestring:


        crie um nó do Grafo -->



Nó:
Aresta:

Transformar Paradas

## Linhas de Onibus em Subgrafos



## Junção dos SubGrafos em um único Grafo




## Replicar para todo o Brasil




## Referências

- 1. [Semob](https://semob.df.gov.br/)

## Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criação Pseudocódigo  | Leonardo Vitoriano | - | 03/08 |



