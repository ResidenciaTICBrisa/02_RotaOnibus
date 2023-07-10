# Requisitos 

## 1. Elicitação

A partir da técnica de elicitação de requisitos Brainstorming, realizado pelo equipe na [Ata de Reunião 26/06/23](../AtaReuniao/AtaReuniao_2606.md), foi possível identificar os seguintes requisitos funcionais e não funcionais encontradas, respectivamente, nas Tabelas 1 e 2. 

Requisitos Funcionais:

| Código | Requisito |
|   -    |    -      |
|   RF1  | A API deve receber as coordenadas do ponto partida e do ponto chegada |
|   RF2  | A API deve validar as coordenadas dos pontos de entrada |
|   RF3  | A API deve calcular a menor rota, por rodovias, entre os pontos de entrada |
|   RF4  | A API deve retornar a menor rota, por rodovias, entre os pontos de entrada |
<p align="center">Tabela 1. Requisitos Funcionais</p>

Requisitos Não Funcionais:

| Código  | Requisito |
|   -     |    -      |
|   RNF1  | A API deve ser desenvolvida em Python usando o Framework Django Rest |
|   RNF2  | A API deve ser RESTful |
|   RNF3  | A API deve possui tempo de resposta de até 20 segundos |
|   RNF4  | A entrada dos pontos na API devem ser um arquivo JSON |
|   RNF5  | A entrada dos pontos na API devem conter a latitude e longitude |
|   RNF6  | A saída da da API deve ser um arquivo JSON  |
|   RNF7  | Os pontos de retorno do arquivo JSON devem conter a latitude e longitude |
|   RNF8  | Os pontos de retorno do arquivo JSON devem ser paradas de onibus existentes vida real |
|   RNF9  | A API deve considerar trânsito e horários de pico, em tempo de execução |
<p align="center">Tabela 2. Requisitos Não Funcionais</p>


## 2. Backlog

O backlog do produto é a lista de itens (histórias de usuário, bugs, deveres) usados pelo time de software para coordenar o trabalho
a ser feito. Ele serve como ponte entre a geração e implementação das **histórias de usuário**.

No Scrum temos dois backlogs:

- Product backlog: refere-se a uma lista contendo as necessidades gerais do produto, onde o gerente ou Product owner, define de acordo com a priorização feita pelo cliente. Durante as reuniões de Sprint Planning o gerente apresenta o backlog para a equipe e é definido quais serão as tarefas da Sprint.

- Sprint backlog: refere-se a uma lista contendo artefatos menores,de uma sprint , que agrega valor a cada nova sprint para o cliente, diferente.

Histórias de usuário descrevem funcionalidades com o objetivo de agregar valor ao cliente e à equipe de desenvolvimento.
Cohn propõe a forma de estruturar uma US (sua gramática), que é a mais utilizada pelos desenvolvedores. A estrutura
proposta por Cohn descreve pontos fundamentais dos requisitos do usuário, sendo: tipo de usuário; objetivo; e a razão
do requisito descrito.

Alguns dos motivos para utilizar hitórias de usuários são (Cohn, 2004):

- Enfatizam comunicação verbal;
- São compreensivas para todos;
- Do tamanho certo para planejamento;
- Trabalham com desenvolvimento iterativo;
- Incentivam o adiantamento dos detalhes;
- Estimulam o projeto participativo.

Para complementar a escrita das histórias de usuário são descritos os critérios de aceitação, os quais tem grande importância
para os desenvolvedores, pois definem pontos que devem ser considerados durante a implementação. 

### 2.1 Épicos

Um épico é uma história de usuário que ainda não foi detalhada, é muito grande ou ainda possui muita incerteza e portanto não pode ser transformada em incremento do produto. O épico deve ser separado em histórias de usuário menores. 

### Épico 01: Serviço de rotas

| História de Usuário  | Eu, como usuário, gostaria de... | Para poder...                         | Prioridade |
| -----------------|----------------------------------|---------------------------------------|------------|
| US1 |  Criar uma página                 | Escrever minhas anotações             | M          |


## Requisitos Não Funcionais



## Histórico de Versão

| Versão | Alteração |  Responsável  | Revisor | Data  |
| ------ | :-------: | :-----------: | :-----: | :---: |
|  1.0   | Criando da introdução e estrutura épicos | Leonardo Vitoriano |  -   | 21/06/23 |