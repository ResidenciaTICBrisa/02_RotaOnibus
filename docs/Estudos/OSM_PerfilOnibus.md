# Open Street Map - Perfil Ônibus

## 1. Introdução 

Na documentação do OSMnx, não existe uma separação explícita de perfis tais como existem nos outros motores de busca e roteamento (OSRM e ORS). Porém, no Open Street Map é possível escolher qual o tipo de rede do Grafo será gerado, a partir de uma região definida, ou seja, pode ser criado um Grafo que mapea o Distitro Federal com todas as ruas para pedestre.


por exemplo:  ter a   baixar e criar gráficos a partir dos dados do OpenStreetMap com o módulo **osmnx.graph** 

## 2. Tipos de Rede no OSM

No módulo osmnx.graph é possível baixar e criar grafos a partir dos dados do OpenStreetMap. E nesse módulo que possuí o parâmetro *network_type* (tipo de rede) para criar o Grafo de uma região delimitada.

A listagem dos tipos de redes, encontrados na documentação, estão listados a seguir:

- 'drive' - obtém ruas públicas dirigíveis (mas não estradas de serviço).
- 'drive_service' - obtém ruas dirigíveis, incluindo estradas de serviço.
- 'walk' - obtém todas as ruas e caminhos que os pedestres podem usar (esse tipo de rede ignora a direcionalidade de mão única).
- 'bike' - obtém todas as ruas e caminhos que os ciclistas podem usar.
- 'all' - baixa todas as ruas e caminhos OSM não privados (este é o tipo de rede padrão, a menos que você especifique um diferente).
- 'all_private' - baixa todas as ruas e caminhos OSM, incluindo os de acesso privado.

## 3. Diferença entre 'drive' e 'drive_service'

Os tipos de rede 'drive' e 'drive_service' são parecidos mas não idênticos. O tipo de rede 'drive_service' seria o mais apropriado para o objetivo da API a ser desenvolvida, pois abrange rotas que os ônibus transitam. A diferença entre os tipos de rede podem ser identificados a seguir:


1. '**drive**': Quando você define network_type='drive', o OSMnx recuperará a rede de ruas para veículos motorizados, incluindo todas as estradas dirigíveis, como ruas, rodovias e vias expressas. Inclui todas as estradas acessíveis aos carros, mas pode não necessariamente incluir informações específicas de transporte público, como paradas de ônibus. <br>
A rede 'drive' é adequada para roteamento geral de carros, mas pode não ser suficiente para roteamento detalhado de ônibus, especialmente se você precisar considerar pontos de ônibus, faixas exclusivas para ônibus ou outros recursos relacionados ao transporte público. 
2. '**drive_service**': Quando você define network_type='drive_service', o OSMnx recuperará a rede de ruas para veículos motorizados, semelhante à opção 'drive'. No entanto, adiciona recursos adicionais, como estradas de serviço, becos e calçadas. Essas vias de serviço podem incluir pontos de acesso a pontos de ônibus, pontos de entrega e outros recursos relacionados ao serviço. <br> 
A rede 'drive_service' é mais detalhada do que a rede 'drive' e pode incluir algumas informações sobre paradas de ônibus. Esta opção é mais apropriada se você deseja obter informações de rota para ônibus que acessam determinados pontos de serviço, como pontos de ônibus e outras instalações de serviço.

## 4. Conclusão 

É possível precisar de informações muito detalhadas sobre os pontos de ônibus, como suas localizações exatas e conexões com a rede viária, 'drive_service' pode ser mais apropriado. Esta opção incluirá estradas de serviço e outros recursos que provavelmente serão relevantes para pontos de ônibus.

## 5. Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criando documentação perfil ônibus OSM | Leonardo Vitoriano | - | 26/07 |












