# Documentação da Interface de Programação de Aplicações (API) para Rotas de Ônibus

## Sumário Executivo

O presente documento tem como objetivo oferecer uma visão geral técnica e detalhada da Interface de Programação de Aplicações (API) desenvolvida para otimização de itinerários do sistema de transporte público por ônibus. A API foi projetada para calcular rotas eficientes utilizando-se de um conjunto de operações algorítmicas avançadas. A execução do serviço pode ser resumida nos seguintes procedimentos fundamentais:

- Determinação da Parada Inicial: Localização da estação de ônibus mais próxima em relação às coordenadas geográficas fornecidas pelo usuário, servindo como ponto de partida da rota.

- Cálculo da Rota Ótima: Implementação do algoritmo de Dijkstra para a identificação das sequências de paradas de ônibus que configuram o itinerário mais eficiente. Este processo prioriza a minimização de transferências entre diferentes linhas de ônibus.

- Traçado do Percurso: Emprego da biblioteca OSMNX para mapear o trajeto entre as paradas de ônibus selecionadas, garantindo a precisão do percurso a ser seguido.

```
{
    "baldeacao_orig": "<caminho_a_pe_inicial>",
    "rota_veicular": "<itinerario_do_onibus>",
    "baldeacao_dest": "<caminho_a_pe_final>",
    "paradas": "<lista_de_paradas_de_onibus>"
}
```

- baldeacao_orig: Representa o segmento percorrido a pé do ponto de origem até a primeira parada de ônibus.

- rota_veicular: Denota o itinerário percorrido pelo ônibus.

- baldeacao_dest: Corresponde ao trecho final percorrido a pé da última parada de ônibus até o destino final.

- paradas: Lista todas as paradas de ônibus que compõem a rota.

## Instruções para Implantação e Execução

A infraestrutura da API foi construída empregando a biblioteca Python FAST API. Para a execução do serviço, é necessário utilizar o seguinte comando de linha de terminal:

```
uvicorn main:app --reload
```

Antes da ativação da API, é imprescindível que o grafo representativo da rede viária da região de interesse esteja devidamente posicionado no diretório de trabalho da API. A construção deste grafo pode ser realizada por meio da execução do script contido no notebook Jupyter denominado "gerarGrafos.ipynb".

São fornecidos dois scripts distintos: um para a geração do arquivo `distrito_federal.graphml` e outro para o `leve_distrito_federal.graphml`. A principal distinção entre eles reside na configuração do parâmetro `simplify` na função graph_from_place. Quando definido como `False`, o grafo gerado apresenta uma fidelidade superior na representação de curvas, acarretando, contudo, um aumento significativo no volume de dados processados, o que pode impactar o desempenho da API. Portanto, recomenda-se a utilização do parâmetro `simplify` configurado como True para otimizar a performance.

Com o grafo adequadamente preparado, o comando supracitado iniciará a API, que estará operacional na porta definida por padrão pelo FAST API.


## Procedimento de Teste da API

Para a verificação e validação da funcionalidade da API, disponibilizamos o script teste.py. Este script permite o teste integral da API, incluindo a geração de um arquivo HTML que ilustra graficamente a rota calculada. Para realizar o teste, é necessário especificar as coordenadas de origem e destino no formato de latitude e longitude, conforme o exemplo abaixo:

```
lat_origin = -15.989444964529529
lon_origin = -48.044418962814866

lat_destiny = -15.818353856600432
lon_destiny = -47.87465146311891
```

A execução deste script resultará na demonstração prática da capacidade da API de gerar um itinerário otimizado, considerando as variáveis de entrada definidas pelo usuário.
