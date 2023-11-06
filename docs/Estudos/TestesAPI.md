# Testes da API

Os testes em uma API (Interface de Programação de Aplicativos) são um aspecto crítico do desenvolvimento de software. Eles desempenham um papel fundamental na garantia de que a API funcione conforme o esperado, seja confiável, segura e atenda aos requisitos do usuário. Aqui estão alguns pontos-chave sobre testes na API e sua importância:

1. Verificação de Funcionalidade:

    Os testes de funcionalidade são projetados para garantir que a API realize todas as operações especificadas em sua documentação. Isso inclui testar cada endpoint, método e funcionalidade para garantir que eles funcionem conforme o esperado.

2. Garantia de Qualidade:

    Os testes ajudam a garantir a qualidade da API, detectando e corrigindo erros e problemas antes que eles cheguem aos usuários finais. Isso inclui a identificação de bugs, problemas de desempenho e vulnerabilidades de segurança.

3. Conformidade com Padrões:

    Os testes podem verificar se a API está em conformidade com padrões e práticas recomendadas. Isso inclui conformidade com protocolos (por exemplo, REST, SOAP) e padrões de segurança.

4. Testes de Integração:

    Os testes de integração verificam se a API funciona corretamente quando interage com outros sistemas ou serviços, garantindo que todos os componentes se comuniquem de maneira eficaz.

5. Testes de Unidade:

    Os testes de unidade se concentram em partes individuais da API, como funções ou métodos específicos. Eles são essenciais para garantir que cada parte da API funcione isoladamente antes de serem integrados em um sistema maior.

6. Testes de Desempenho:

    Os testes de desempenho avaliam o desempenho da API, incluindo sua capacidade de resposta, escalabilidade e latência. Isso é crucial para garantir que a API funcione bem sob carga.

7. Testes de Segurança:

    Os testes de segurança são fundamentais para identificar e corrigir vulnerabilidades que possam ser exploradas por invasores. Isso ajuda a proteger os dados e a integridade da API.

8. Testes Automatizados:

    A automação de testes é uma prática recomendada, permitindo a execução rápida e repetida de testes sempre que houver alterações no código. Isso ajuda a identificar problemas mais cedo e acelera o ciclo de desenvolvimento.

9. Documentação Viva:

    Os testes podem servir como parte da documentação viva da API, fornecendo exemplos práticos de como usá-la. Isso é útil para os desenvolvedores que desejam integrar a API em seus aplicativos.

10. Melhoria Contínua:
    
    Os testes oferecem feedback contínuo sobre o funcionamento da API, possibilitando melhorias iterativas. À medida que os requisitos evoluem, os testes ajudam a garantir que a API continue atendendo às necessidades do usuário.

Em resumo, os testes desempenham um papel crítico na garantia de que uma API seja robusta, confiável, segura e funcional. Eles são essenciais para a qualidade do software e para a satisfação do usuário. Portanto, é importante investir tempo e recursos significativos em estratégias de teste eficazes ao desenvolver uma API.

## Testes de Sistema

Os testes de sistema em uma API (Interface de Programação de Aplicativos) fazem parte de um conjunto mais amplo de estratégias de teste que visam avaliar se a API, como um todo, atende aos requisitos e às expectativas estabelecidos. Esses testes não estão preocupados apenas com as funcionalidades individuais da API, mas também com sua capacidade de funcionar como uma unidade coesa no contexto de um sistema maior.

### Issue de Testes de Sistema

A [issue 47](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/47) descreve como os testes devem ser realizados, bem como suas categorias de teste. A descrição da issue pode ser encontrada a seguir:

Cada Teste de Sistema deve passar a Entrada: pontos de Origem e Destino, ambos com latitude e longitude, e verificar a Saída, rota gerada pela API, com uma rota gerada pelo Moovit ou Google Maps. A verificação da Saída deve seguir as seguintes etapas:

- Verificar as linhas de ônibus geradas pela API.
- Verificar a quantidade de linhas de ôninus retornada pela API.
- Verificar se a rota da API está parecida com rota do Moovit ou Google Maps.

Os Testes de Sistema pode ser categorizados da seguinte forma:

- Categoria A: Testes de Sistema que seja possível chegar da Origem ao Destino com apenas 1 Linha de ônibus.
- Categoria B: Testes de Sistema que seja possível chegar da Origem ao Destino com Baldeação (trocas apenas de ônibus durante a rota).
- Categoria C: Testes de Sistema que seja possível chegar da Origem ao Destino com Baldeação de Ônibus (trocas de ônibus durante a rota) e Baldeação a pé ( andar de uma parada até a outra ).

## Testes Categoria A

A seguir, estão listados os casos de teste executados:

| Origem          | Destino         | Coordenadas Origem        | Coordenadas Destino       |
|-----------------|-----------------|---------------------------|---------------------------|
| FGA             | Recanto Q.801       |-15.989444964529529, -48.044418962814866 |-15.919392602743956, -48.051763232078855    |
| FGA             | Riacho Fundo 2      | -15.989444964529529, -48.044418962814866| -15.905081947923286, -48.05133180235249     |
| Recanto         | Nucleo Bandeirante  | -15.902369945850355, -48.06114590425264 | -15.87053919722047, -47.970845583947956     |
| Recanto         | Taguatinga shopping | -15.902369945850355, -48.06114590425264 | -15.838687092189542, -48.043740029911895    |
| Vicente Pires   | taguatinga Shopping | -15.803336993126374, -48.01783002446128 | -15.838687092189542, -48.043740029911895    |


### Teste 1 - FGA - Recanto Q.801

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/FGA-rec801G.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/FGA-rec801API.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>

### Teste 2 - FGA - Riacho fundo 2

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/FGA-riacho2G.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/FGA-riacho2API.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>

### Teste 3 - Recanto - Nucleo Bandeirante

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/Rec-nbandG.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/rec-nbandAPI.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>

### Teste 4 - Recanto - Taguatinga shopping

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/Rec-TshopG.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/Rec-TshopAPI.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>

### Teste 5 - Vicente Pires - Taguatinga shopping

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/Vic-tshopG.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/Vic-tshopAPI.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>


## Testes Categoria B

A seguir, estão listados os casos de teste executados:

| Origem          | Destino         | Coordenadas Origem        | Coordenadas Destino       |
|-----------------|-----------------|---------------------------|---------------------------|
| FGA             | Recanto Q.102       |-15.989444964529529, -48.044418962814866 |-15.919392602743956, -48.051763232078855    |
| Recanto         | Sobradinho          | -15.902369945850355, -48.06114590425264 | -15.649050315402839, -47.79407366681607     |
| Recanto         | Planaltina          | -15.902369945850355, -48.06114590425264 | -15.586737032575579, -47.68191991430089     |

## Teste 1 - FGA - Recanto Q.102

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/FGA-rec102G.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/FGA-recQ102API.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>

## Teste 2 - Recanto - Sobradinho

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/rec-sobraG.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/rec-sobAPI.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>

## Teste 3 - Recanto - Planaltina

<div style="display: flex; justify-content: space-between;">
    <div style="text-align: center;">
        <img src="./assets/Testes/REC-planG.png" alt="Google Maps" style="width: 45%;" />
        <p>Google Maps</p>
    </div>
    <div style="text-align: center;">
        <img src="./assets/Testes/Rec-planalAPI.png" alt="API" style="width: 45%;" />
        <p>API</p>
    </div>
</div>



## Histórico de Versão

| Versão |      Alteração       | Responsável  | Revisor | Data  |
| :----: | :------------------: | :----------: | :-----: | :---: |
|  1.0   | Criação do documento, testes de sistema e issue de testes | Leonardo Vitoriano |    -    | 06/11 |
|  1.1   | 5 Testes categoria A, 3 categoria B | Natália |    -  | 06/11 |