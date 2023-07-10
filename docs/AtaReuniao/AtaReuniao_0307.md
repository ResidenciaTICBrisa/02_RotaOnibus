# Ata de Reunião do Dia 03/07/2023

## 1. Data, Horário, Duração e Local

&emsp;&emsp;As informações sobre data, horário, duração e local da reunião estão detalhadas a seguir:
- **Data**: 03/07/2023
- **Horário Início**: 14:00.
- **Duração**: 1 hora e 20 minutos.
- **Local**: Laboratório cocreation, Presencial.

## 2. Participantes

&emsp;&emsp;Na reunião, **todos** os integrantes do grupo participaram, sendo então os presentes:

- João Leles
- Leonardo Vitoriano
- Lucas Lopes Frazao
- Luiz Felipe
- Natalia Martimon

## 3. Pontos de Discussão Importantes

&emsp;&emsp; 

Témino da sprint definida pelo grupo no dia 26/06/23, com as issues descritas na tabela 1.

| Identificador (*Issue n*) | *Issue* | Integrante(s) responsável(eis) |  
| -   | - | - | 
| Issue 2  | Realizar Ata de reunião 26/06/2023 | Leonardo |
| Issue 3  | Estudar sobre grafos até entender o algoritmo dijkrstra  | Todos |
| Issue 4  | Estudar sobre o Django e Django Rest Framework | Leonardo e Lucas |
| Issue 5  | Estudar sobre o funcionamento do DFNoPonto e semelhantes. | João, Luiz, Natália |
<p align="center">Tabela 1. Issues Sprint 1</p>

 As issues 2, 4 e 5 foram concluídas e a issue 3 foi mantida.

Para a criação da nova sprint precisava-se de uma segunda reunião com o cliente para o esclarecimento de algumas dúvidas da equipe, porém como a segunda reunião com o cliente ainda não aconteceu e está marcada para dia 04/07/2023, a equipe ainda não conseguiu definir a nova sprint para andamento do projeto.

As dúvidas da última semana foram mantidas e podem ser encontradas na tabela 2, onde cada dúvida tem o seu identificador *Dn* para rastreabilidade, sendo *D* de Dúvida e *n* o número da dúvida.

| Identificador (*Dn*) | Dúvida |
| -   | - |
| D1  | Quem é o nosso cliente final?<br>1) Civil que irá utilizar o aplicativo e o aplicativo terá de informar o caminho até algum ponto de onibus<br>2) empresa que precisa definir uma rota para seus onibus |
| D2  | O sistema vai operar de maneira interestadual ou será utilizado por alguma empresa que opera de forma regional? |
| D3  | Existe alguma especificação para a entrada e saída dos dados? (Ex.: csv, json) |
| D4  | Entender diretamente o que temos que fazer:<br>1) As rotas de onibus já existem e devemos otimiza-las<br>2) Devemos criar uma nova rota já otimizada  |
<p align="center">Tabela 2. Dúvidas</p>

As tarefas da primeira entrega, se mantiveram para serem formalizadas com o cliente. Sendo assim, as tarefas da **Entrega 1** são visualizadas na Tabela 3, onde cada tarefa tem o seu identificador *Tn* para rastreabilidade, sendo *T* de Tarefa e *n* o número da tarefa.

| Identificador (*Tn*) | Tarefa |
| -   | - |
| T1  | Traçar uma rota entre 2 pontos (mais simples possível) |
| T2  | Transformar esse serviço em uma API |
| T3  | Um pequeno frontend para plotar os dados recebidos da API |
| T4  | API operando somente no DF  |
<p align="center">Tabela 3. Entrega 1</p>

Foram apresentados e discutidos alguns requisitos funcionais (presentes na tabela 4 ) e não funcionais (presentes na tabela 5 ) para serem validados com o cliente, onde cada tarefa tem o seu identificador *Rn* para rastreabilidade, sendo *R* de Requisito e *n* o número do requisito.

| Identificador (*Rn*) | Requisito funcional |
| -   | - |
| R1  | Eu, como usuário, gostaria de enviar 2 pontos no mapa do brasil, para que eu pudesse receber a menor rota de onibus entre os pontos|
| R2  | Receber os pontos de origem e destino: A API deve permitir que o usuário envie os pontos de origem e destino, especificando as coordenadas de latitude e longitude.|
| R3  | Validar os pontos: A API deve realizar a validação dos pontos recebidos, garantindo que sejam válidos e estejam dentro do território do Brasil.|
| R4  | Calcular a menor rota: A API deve implementar um algoritmo para calcular a menor rota de ônibus entre os pontos fornecidos. Isso pode envolver o uso de algoritmos de roteirização, como o algoritmo de Dijkstra, por exemplo.|
| R5  | Retornar a rota calculada: A API deve retornar a rota de ônibus calculada ao usuário, normalmente em um formato estruturado, como JSON. A rota pode incluir informações como pontos intermediários, distâncias, tempos de viagem estimados e instruções de direção.|
| R6  | Considerar informações de transporte público: A API pode incorporar informações sobre horários e itinerários de ônibus para fornecer uma rota precisa que leve em conta as opções disponíveis de transporte público.|
| R7  | Tratar exceções e erros: A API deve ser capaz de lidar com situações excepcionais, como pontos inválidos, falta de rota disponível ou erros de processamento, retornando mensagens de erro apropriadas para o cliente.|
<p align="center">Tabela 4. Requisito funcional</p>

| Identificador (*Rn*) | Requisito não funcional |
| -   | - |
| R1  | A API deve ser desenvolvida em Python usando o Framework Django Rest|
| R2  | API deve receber a solicitação e respondê-la em até 30 segundos|
| R3  | API deve ser RESTful|
| R4  | A entrada dos pontos na API devem ser um arquivo JSON|
| R5  | A entrada dos pontos na API devem conter a latitude e longitudde|
| R6  | A saída de retorno da API deve ser um arquivo JSON |
| R7  | Os pontos de retorno do arquivo JSON devem conter a latitude e longitude|
| R8  | Os pontos de retorno do arquivo JSON devem ser paradas de onibus existentes vida real|
| R9  | A API deve considerar transito e horários de pico|

<p align="center">Tabela 5. requisito não funcional</p>


## 4. Decisões

&emsp;&emsp; A reunião com o cliente foi marcada para o dia 04/07/2023, e foi decidido que após essa reunião outra será marcada para estabelecer as issues da Sprint 2. 

## 5. Histórico de Versão
| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criando Ata de Reunião 2  | Natália Martimon | - | 05/07 |




