# Ata de Reunião do Dia 01/08/2023

## 1. Data, Horário, Duração e Local

&emsp;&emsp;As informações sobre data, horário, duração e local da reunião estão detalhadas a seguir:
- **Data**: 01/08/2023.
- **Horário Início**: 17:00.
- **Duração**: 1 hora.
- **Local**: Remoto (Microsoft Teams).

## 2. Participantes

&emsp;&emsp;Na reunião, **todos** os integrantes do grupo participaram, sendo então os presentes:

- João Leles
- Leonardo Vitoriano
- Lucas Lopes Frazao
- Luiz Felipe
- Natalia Martimon 

## 3. Pontos de Discussão Importantes

&emsp;&emsp;Na reunião do dia 01/08/23, foi importante para validar com o cliente, o progresso que a equipe realizou na Sprint passada. A princípio, as issues designadas para a equipe foram as seguintes:

| Identificador (*Issue n*) | *Issue* | Integrante(s) responsável(eis) |  
| -   | - | - | 
| [Issue 24](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/24)  | Estudo sobre o perfil de busca nos motores | Todos |
<p align="center">Tabela 1. Issues Sprint 4</p>

Porém, depois de uma Reunião com a Carla (Coordenadora do Lappis) na quinta (27/07), foi debatido que será necessário um **Pré-processamento** dos [Shape Files](https://residenciaticbrisa.github.io/02_RotaOnibus/#/./Estudos/EstudoShapeFiles?id=_1-o-que-s%c3%a3o-arquivos-shapefiles) tanto das Paradas de ônibus quanto das Rotas de ônibus do [Semob](https://semob.df.gov.br/) (Secretaria de Trasnporte e Mobilidade) do Distrito Federal. A mudança das issues da Sprint pode ser visualizada na Tabela 2.

| Identificador (*Issue n*) | *Issue* | Integrante(s) responsável(eis) |  
| -   | - | - | 
| [Issue 18](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/18)  | Estudar sobre o shapefile | Todos |
| [Issue 19](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/19)  | Estudar o CSV gerado pelo Semob das paradas | Leonardo e João |
| [Issue 20](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/20)  | Estudar o CSV gerado pelo Semob das rotas | Natália e Luiz |
<p align="center">Tabela 2. Issues Sprint 4</p>

O objetivo desse **Pré-processamento** é reduzir o grande volume de Dados que existem no Shape File das Rotas de ônibus, pois as rotas envolvem todo o trajeto do ônibus o qual não é de interesse do usuário final, visto que o usuário almeja apenas, dado uma parada de ônibus de origem, saber qual a linha de ônibus que chegue à parada de ônibus de seu destino. Sendo assim, essa integração dos Shape Files visa definir para todas a linhas de ônibus, quais são as todas paradas que estão contidas nessas linhas. 

Dessa forma, o resultado do **Pré-processamento** seria um Grafo direcional. Os nós do Grafo seriam as paradas de ônibus e todos os metadados associados à elas, tais quais: latitudade e longitude, nome, identificador, entre outros. As arestas do Grafo seriam as ligações direcionadas entre as paradas, bem como os metadados das arestas: distância, linhas de ônibus, dentro outros.   

## 4. Decisões

&emsp;&emsp; Depois de validar as mudanças da issue com o cliente e mostrar os avanços realizados com o [notebook](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/blob/main/docs/Notebooks/testeParadasLinhasLuiz.ipynb), as issues da próxima Sprint estão descritas na Tabela 3.

| Identificador (*Issue n*) | *Issue* | Integrante(s) responsável(eis) |  
| -   | - | - | 
| [Issue 21](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/21)  | Criar ata da reunião do dia 01/08/23 | Leonardo |
| [Issue 22](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/22)  | Criar Linestring de todas as linhas do DF | Luiz |
| [Issue 23](https://github.com/ResidenciaTICBrisa/02_RotaOnibus/issues/23)  | Criar Grafo Direcional de uma linha de onibus | Leonardo, João, Natália e Luiz |
<p align="center">Tabela 3. Issues Sprint 5</p>


## 5. Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criando Ata de Reunião  | Leonardo Vitoriano | - | 02/08 |

