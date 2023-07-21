# RoadMap

## Entrega 1 (17/07 - 31/07):

### Tarefa 1: Configurar o ambiente do Python com as bibliotecas necessárias.

- Instalar Python e as dependências do projeto.

*Plotagem do mapa (Frontend)*

- Leaflet

*Geração da rota*

- Routingpy’s (Contém todos?)
- Osmnx
- Osrm
- Network-x
- Open Route Service
- Google or-tools
- GeoPy
- Backend
- Django rest framework
- FastAPI (recomendação do Eduardo)
- Flask

*Realizar testes básicos para verificar se o ambiente está funcionando corretamente.*

### Tarefa 2: Armazenar o Grafo Estático necessário para os cálculos futuros.

- Definir a estrutura do Grafo Estático.
- Recomendação: Geofabrik (http://download.geofabrik.de/south-america/brazil.html)
- Criar um mecanismo para carregar e armazenar o Grafo.

### Tarefa 3: Armazenar os resultados e testes dos estudos.

## Entrega 2 (01/08 - 31/08):

### Tarefa 1: Estudar sobre a implementação.

- Documentar testes com as ferramentas utilizadas.
- Calcular diferentes rotas levando em conta tempo de execução (rotas alternativas dependendo do trânsito).

## Entrega 3 (01/09 - 30/09):

### Tarefa 1: Implementar a funcionalidade para receber dois pontos (origem e destino) como entrada.

- Criar uma interface para que o usuário possa fornecer os pontos de origem e destino.
- Validar e processar as entradas recebidas.
- Enviar para a API os dois pontos.
- Recomendação: React

### Tarefa 2: Calcular a rota rodoviária entre os dois pontos usando o Grafo Estático armazenado anteriormente.

- Utilizar algoritmos de busca em grafos oferecidos pelas bibliotecas para encontrar a rota.

### Tarefa 3: Implementar a funcionalidade para retornar a menor rota entre os dois pontos como um arquivo JSON.

- Criar um endpoint na aplicação para gerar o arquivo JSON com as informações da rota.
- Testar e validar a geração correta do arquivo JSON.

### Tarefa 4: Plotar o mapa com os dois pontos e a rota calculada.

- Integrar com uma biblioteca de visualização de mapas (Leaflet por exemplo)
- Plotar os pontos de origem e destino no mapa.
- Desenhar a rota encontrada no mapa.

### Tarefa 5: Plotar a menor rota no mapa, incluindo os dois pontos e informações adicionais.

- Aprimorar a visualização do mapa para incluir informações detalhadas da rota.
- Adicionar dados como distância, tempo estimado e outras informações relevantes.

## Entrega 4 (01/10 - 31/10):

### Tarefa 1: Mapear as linhas de ônibus existentes na região de interesse.

- Obter dados das linhas de ônibus de uma fonte confiável.
- Estruturar os dados para uso no sistema.

### Tarefa 2: Adaptar o sistema para retornar a rota que inclua as linhas de ônibus disponíveis.

- Modificar a lógica de cálculo de rota para considerar as linhas de ônibus disponíveis.
- Identificar as opções de rota com transporte público mais adequadas.

## Entrega 5 (01/11 - 24/11):

### Tarefa 1: Realizar testes abrangentes em todas as funcionalidades do sistema.
- Criar casos de teste para cada funcionalidade implementada.
- Executar os testes e corrigir possíveis problemas identificados.

### Tarefa 2: Preparar o ambiente de produção para o deploy da aplicação.
- Configurar um servidor ou plataforma adequada para o deploy.
- Preparar o banco de dados e o ambiente de produção.

### Tarefa 3: Realizar o deploy do sistema em um ambiente de produção.
- Efetuar o deploy da aplicação no ambiente preparado.
- Realizar testes finais após o deploy para garantir que tudo esteja funcionando corretamente.
