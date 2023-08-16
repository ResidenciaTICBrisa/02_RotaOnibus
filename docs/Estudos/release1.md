# Release 1

## RELATO DE EXPERIÊNCIA

### Contexto

#### Introdução
No cenário atual, a prestação de serviços de planejamento de rotas de ônibus é majoritariamente controlada por empresas privadas, seguindo o modelo de negócio "Mobility as a Service". Enquanto soluções de rotas de código aberto, como o Valhalla, já estão disponíveis, elas se concentram principalmente em modos de transporte como carros, pedestres e bicicletas. Contudo, o desafio que encaramos é adaptar essas soluções de código aberto de modo a satisfazer as exigências das rotas de ônibus. 

#### O Cenário Atual
No cenário atual, as empresas privadas dominam o mercado de serviços de rotas de ônibus. Essa abordagem tem suas limitações e pode ser menos flexível para acomodar as demandas em constante mudança dos usuários. Além disso, a falta de opções open source específicas para rotas de ônibus torna o ecossistema menos acessível para desenvolvedores, transparente e impede ajustes que atendam um determinado público.

#### O Potencial das Soluções Open Source
Por outro lado, as soluções open source oferecem um potencial considerável os serviços de rotas de ônibus. Ferramentas como Valhalla, OSRMX, OSM, OpenRouteService e OpenStreetMap baseiam-se na colaboração global para fornecer soluções de rota altamente personalizáveis e transparentes. Essas ferramentas oferecem a flexibilidade necessária para adaptar as soluções às demandas específicas das rotas de ônibus.

#### Nosso Objetivo
Em resumo, o projeto tem como objetivo final criar um sistema que seja capaz de sugerir a rota ótima para um usuário final, considerando dois pontos de partida e de chegada, e, se necessário, diferentes opções de linhas de ônibus durante o trajeto.


### Desafios

Durante o decorrer deste projeto, nos deparamos com uma série de desafios significativos. Inicialmente, nossa principal tarefa era adquirir uma compreensão profunda do contexto do projeto e assimilar o conhecimento sobre as tecnologias que seriam implementadas. Após uma série de encontros com nosso cliente, fomos direcionados a explorar o universo dos motores, com ênfase em identificar um motor que fosse perfeitamente compatível com as nossas necessidades.

Nesse processo de pesquisa, destacou-se a lacuna evidente na disponibilidade de um perfil de motor direcionado especificamente para ônibus. Isso nos impulsionou a estabelecer como meta a criação de um novo perfil, integrando-o a um dos motores já existentes. No entanto, uma reunião subsequente com a Professora Carla nos guiou na direção correta, evidenciando a necessidade primordial de lidar com a formatação dos dados referentes às rotas e paradas de ônibus. Somente após a criação de um grafo direcionado com base nesses dados é que deveríamos concentrar nossos esforços em perfis de motor.

Um dos desafios mais substanciais que enfrentamos até o momento foi essa mudança de enfoque imposta por essa reorientação estratégica. As linhas de ônibus fornecidas nos apresentaram uma complexidade notável, com seus múltiplos pontos que não se alinhavam com as paradas de ônibus existentes. Transformar essas paradas em nós para otimização das rotas surgiu como um desafio adicional, trazendo à tona a complexidade subjacente.

À medida que avançamos, temos pela frente uma série de desafios prospectivos. Um deles consiste em mapear com abrangência todas as paradas e linhas de ônibus em todo o território nacional, com especial atenção para verificar a compatibilidade dos formatos de arquivos utilizados com os padrões do Distrito Federal.



### Solução proposta

#### Processamento de Paradas e Rotas de ônibus no Distrito Federal

A Secretaria de Transporte e Mobilidade (Semob) do Distrito Federal fornece dados sobre paradas e rotas de ônibus em diversos formatos, sendo o Shapefile o mais relevante para este projeto. Esse formato descreve as paradas com coordenadas (latitude e longitude) e as linhas de ônibus com trajetos completos em forma de LINESTRING.

O arquivo de paradas, ao ser transformado em GeoDataFrame, apresenta as paradas com coordenadas geográficas em POINT. Esse dado é vital para identificar as paradas nas linhas de ônibus.

Já o arquivo de linhas, também transformado em GeoDataFrame, traz trajetos em LINESTRING, representando o percurso completo de cada ônibus. No entanto, a ênfase recai nas paradas, levando a uma simplificação da informação, considerando somente os pontos onde os ônibus param.

O processo é detalhado em um notebook, onde se concentra em uma linha específica e seus pontos de parada. O script principal itera por cada parada, calculando a distância até a linha de ônibus. Se a distância for menor que um limiar, a parada é registrada, resultando em um novo conjunto de dados.

Em suma, o notebook se concentra na análise de dados de uma linha e nas paradas. O processo identifica paradas próximas e refina os dados para análises futuras.


#### Criar Grafo Direcional das Linhas de Ônibus

Após a etapa inicial de processamento dos dados, um arquivo CSV foi gerado, contendo as paradas de cada linha de ônibus, bem como a ordem que as paradas aparecem em cada linha. Com base nesse DataFrame, a criação do Grafo Direcional foi concebida com o seguinte Pseudocódigo:

Para cada linha (rota) no DataFrame:
- Criar um novo Grafo Direcional chamado subgrafo

Para cada parada na linha:
- Adicionar um nó ao subgrafo para representar a parada
- Armazenar o identificador e coordenada da parada
   	 
Para cada parada de 1 até o penúltimo nó:
- Calcular a distância entre a parada atual e a próxima parada
- Adicionar uma aresta do nó atual para o próximo nó com a distância e o número da linha de ônibus como atributos
   	 
Calcular a distância entre a última parada e a primeira parada
- Adicionar uma aresta do último nó para o primeiro nó com a distância como atributo
- Adicionar o subgrafo ao grafo principal

Pensamos que cada rota de ônibus seria um subgrafo direcional, que após ser calculado, seria integrado no Grafo geral, o qual contém todas as rotas de ônibus existentes.

Dessa maneira, o Grafo resultante teria nós representando as paradas de ônibus com seus identificadores e coordenadas, e as arestas indicando o número da linha de ônibus e a distância entre os nós conectados.


#### Transformar em API
Depois que o Pré-processamento, que consiste na construção dos subgrafos de todas as linhas de ônibus criados e transformados em um único Grafo Direcional do Distrito Federal, estiver concluído, será possível transformar esse serviço em API.

A API receberá 2 pontos, origem e destino com suas respectivas latitudes e longitudes, e retornará como resposta qual ou quais linhas de ônibus que realizam a rota desejada, bem como todas as coordenadas das paradas que compõem o trajeto completo.

#### Aplicar em escala nacional

Após o serviço de rota de API ser estabilizada para a região do DF, o objetivo seria escalonar para o Brasil inteiro. Com esse fim, será necessário realizar a parte de Pré-processamento para todos os estados do país, de forma que seja possível integrar com a API já em execução.


## RESULTADOS

### Tecnologias escolhidas e justificativa

No âmbito deste projeto, a linguagem de programação Python foi escolhida como base, possibilitando uma abordagem flexível e eficaz para lidar com as complexidades dos dados geoespaciais e análise de rotas.

Dentre as principais bibliotecas do python, destacamos o uso proeminente das bibliotecas GeoPandas e NetworkX. GeoPandas desempenhou um papel crucial, permitindo a manipulação eficiente de arquivos nos formatos SHP e CSV. Sua capacidade de realizar conversões de sistemas de coordenadas foi particularmente valiosa durante o processo de pré-processamento dos dados geoespaciais.

Além disso, a biblioteca NetworkX foi empregada para a criação e análise de grafos que modelaram as rotas e conexões do Distrito Federal, com base nos dados fornecidos pela SEMOB. Esses grafos serão utilizados como representações essenciais para o estudo e otimização das rotas.

Também fizemos uso da biblioteca Pickle para garantir a durabilidade dos grafos que foram gerados. Isso possibilitou exportar os grafos em formatos variados, tornando mais conveniente a eventual integração com mecanismos de cálculo de rotas.

E a biblioteca Shapely também foi utilizada para lidar com operações geométricas, contribuindo para a manipulação e análise de geometrias de forma eficaz.

No contexto da implementação da API, o caminho a seguir ainda não está completamente definido. Duas opções principais estão sendo consideradas: a primeira envolve a transformação dos scripts em Python, utilizando o FastAPI para construir a API. A segunda opção é explorar uma ferramenta que converta diretamente os notebooks que elaboramos em uma API, como sugerido pela Carla. A escolha entre essas alternativas está sendo avaliada para determinar a abordagem mais adequada.

Também é crucial destacar o papel fundamental desempenhado pela biblioteca Folium ao longo de todo esse processo. Graças à sua contribuição, obtivemos uma visualização abrangente e esclarecedora de todos os passos realizados até o momento. Através do Folium, conseguimos traduzir de forma visual nossos estudos, analises e criações, proporcionando uma representação gráfica das informações que nos ajudou a compreender melhor o projeto.


### Produtos entregues até aqui: Funcionalidade/produto funcionando.

Diferentemente de soluções tradicionais que exigem entregas e atualizações constantes, o nosso produto destaca-se por sua abstração. Não estamos atrelados à necessidade de atualizações frequentes como acontece com aplicativos web ou com Inteligências Artificiais que evoluem diariamente.

Estamos confiantes de que a singularidade do nosso produto se traduz em uma entrega robusta. E, com essa proposta de valor, temos a capacidade de aplicar nosso algoritmo em todo o território nacional.

Em fases anteriores, vimos que estávamos indo em uma rota que não era o objetivo do nosso trabalho. Felizmente, com a orientação da Carla, conseguimos redefinir nossa direção e aprofundar nosso entendimento sobre o projeto.

Tendo clarificado nosso objetivo, já realizamos as seguintes entregas:

#### 1) Mapeamento das Paradas de Ônibus nas Linhas do Distrito Federal

A Semob nos fornece diversas bases de dados, incluindo uma sobre as paradas de ônibus e outra sobre os percursos de cada linha de ônibus. Um desafio que identificamos foi a ausência de um mapeamento direto entre as paradas e suas respectivas linhas. Para superar isso, desenvolvemos um algoritmo capaz de estabelecer essa relação, identificando efetivamente as paradas para cada linha de ônibus utilizando aproximações.

#### 2) Conversão das Paradas em Representação Gráfica

Um dos nossos objetivos é representar as paradas dos ônibus em formato de grafo. Após um estudo detalhado, conseguimos aplicar na prática o que foi aprendido, transformando as paradas identificadas no passo anterior em um esquema gráfico.

#### 3) Integração de Múltiplos Grafos em um Arquivo Único

O alcance do nosso projeto exige que todas as paradas de uma rota estejam mapeadas em um grafo representativo de uma determinada região, como o Distrito Federal inteiro. Assim, nos dedicamos a entender como poderíamos consolidar diversos grafos em um único arquivo, e o resultado foi positivo.

#### 4) Próximas Etapas

Com as três etapas anteriores concluídas com sucesso, nos voltamos para os seguintes passos:

- Mapear todas as linhas de ônibus do Distrito Federal com suas paradas (semelhante ao passo 1, pois fizemos nossos estudos e aplicações em uma única rota).
- Transformar essas paradas em representação gráfica (semelhante ao passo 2).
- E finalmente, consolidar todas essas rotas em um único grafo. Ao concluir esta etapa, teremos o arquivo "rotas_df.grafo", permitindo-nos avançar em direção ao nosso objetivo final, conforme discutido no tópico do contexto do projeto.


