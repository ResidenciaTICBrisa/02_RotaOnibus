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

Em resumo, o [notebook](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/blob/main/docs/Notebooks/testeParadas.ipynb) trabalha com dados de uma linha específica e pontos de parada de ônibus. O script principal tem como objetivo, iterar sobre os POINTS de parada de ônibus presentes no shapefile das paradas, calculando a distância entre cada ponto e a linestring de uma linha de ônibus. Se a distância for menor do que um valor específico, o ponto de parada é considerado próximo o suficiente e é registrado. Um novo conjunto de dados é criado com os pontos de parada próximos identificados.

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




Escrever do pré-processamento no DF



    Tratamento das Paradas e Rotas de ônibus do Distrito Federal

    A Secretaria de Transporte e Mobilidade (Semob) do Distrito Federal disponibiliza uma ampla gama de dados relacionados às paradas e rotas de ônibus. Estes dados estão disponíveis em diversos formatos, podendo ser acessados a partir deste link. Para o escopo deste projeto, o formato de maior relevância é o arquivo Shapefile, o qual contém informações detalhadas sobre as paradas e os trajetos dos ônibus.

    No caso do arquivo Shapefile correspondente às paradas, após ser lido e transformado em um GeoDataFrame, ele é composto por informações detalhadas conforme ilustrado na Figura 1. A coluna 'geometry' contém coordenadas em forma de POINT, representando a localização geográfica de cada parada por meio de GPS (latitude e longitude). A importância dessa coluna reside no fato de que será utilizado o seu conteúdo para identificar a presença das paradas nas linhas de ônibus.

    Por outro lado, o arquivo Shapefile que abrange as linhas, após ser lido e processado em um GeoDataFrame, é caracterizado pelas informações delineadas na Figura 2. Agora, a coluna 'geometry' apresenta uma representação LINESTRING, a qual descreve o trajeto completo de um ônibus, abrangendo todos os pontos percorridos até a conclusão da rota. Todavia, para o propósito final, essas informações são excessivas, já que o interesse está centrado nas paradas específicas de cada linha. A tarefa em questão consiste em depurar os pontos dispensáveis presentes na LINESTRING de cada rota, a fim de obter uma versão simplificada que inclui apenas os pontos de parada pelos quais um ônibus trafega.

    O processo de tratamento dos dados referentes às paradas e rotas de ônibus foi detalhadamente documentado em um notebook disponível aqui. Em linhas gerais, o notebook se concentra nos dados de uma linha específica e nos pontos de parada correspondentes. O script principal conduz iterações sobre os pontos de parada no formato POINT presentes no arquivo das paradas, calculando a distância entre cada ponto e a linha de ônibus no formato LINESTRING. Caso essa distância seja menor que um limiar pré-estabelecido, o ponto de parada é considerado próximo o suficiente e é registrado. Esse processo resulta em um novo conjunto de dados contendo os pontos de parada identificados como próximos.

    Em síntese, o notebook oferece uma abordagem focada na análise de dados de uma linha específica e nos pontos de parada de ônibus associados. O procedimento central se baseia na identificação das paradas próximas, por meio da avaliação das distâncias entre os pontos e as linhas de ônibus. O resultado final é a obtenção de um conjunto depurado de pontos de parada, enriquecendo a qualidade das informações disponíveis para análises subsequentes.


Processamento de Paradas e Rotas de ônibus no Distrito Federal


A Secretaria de Transporte e Mobilidade (Semob) do Distrito Federal fornece dados sobre paradas e rotas de ônibus em diversos formatos, sendo o Shapefile o mais relevante para este projeto. Esse formato descreve as paradas com coordenadas GPS e as linhas de ônibus com trajetos completos em forma de LINESTRING.

O arquivo de paradas, ao ser transformado em GeoDataFrame, apresenta as paradas com coordenadas geográficas em POINT. Esse dado é vital para identificar as paradas nas linhas de ônibus.

Já o arquivo de linhas, também transformado em GeoDataFrame, traz trajetos em LINESTRING, representando o percurso completo de cada ônibus. No entanto, a ênfase recai nas paradas, levando a uma simplificação da informação, considerando somente os pontos onde os ônibus param.

O processo está detalhado em um notebook, onde se concentra em uma linha específica e seus pontos de parada. O script principal itera por cada parada, calculando a distância até a linha de ônibus. Se a distância for menor que um limiar, a parada é registrada, resultando em um novo conjunto de dados.

Em suma, o notebook se concentra na análise de dados de uma linha e nas paradas. O processo identifica paradas próximas e refina os dados para análises futuras



Criar Grafo Direcional das Linhas de Ônibus

Após a etapa inicial de processamento dos dados, um arquivo CSV foi gerado, contendo as paradas de cada linha de ônibus, bem como a ordem que as paradas aparecem em cada linha. Com base nesse DataFrame, a criação do Grafo Direcional foi concebida com o seguinte Pseudocódigo:

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

Pensamos que cada rota de onibus seria um subgrafo direcional, que após ser calculado, seria integrado no Grafo geral, o qual contém todas as rotas de onibus existentes.

Dessa maneira, o Grafo resultante teria nós representando as paradas de ônibus com seus identificadores e coordenadas, e as arestas indicando o número da linha de ônibus e a distância entre os nós conectados.


Transformar em API


Depois que o Pré-processamento, que consiste na construção dos subGrafos de todas as linhas de ônibus criados e transformados em um único Grafo Direcional do Distrito Federal, estiver concluído, será possível transformar esse serviço em API. 

A API receberá 2 pontos, origem e destino com suas respectivas latitudes e longitudes, e retornará como resposta qual ou quais linhas de ônibus que realizam a rota desejada, bem como todas as coodernadas das paradas que compôem o trajeto completo.


Aplicar em escala nacional


Após o serviço de rota de API estiver estabilizado para a região do DF, o objetivo seria escalonar para o Brasil inteiro. Com esse fim, é será necessário realizar a parte de Pré-processamento para todos os estados do país, de forma que seja possível integrar com a API já em execução. 



































