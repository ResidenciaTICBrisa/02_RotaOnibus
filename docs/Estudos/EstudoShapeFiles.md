# Arquivos Shapefiles

## 1. O que são arquivos shapefiles?

Arquivos shapefile, ou .shp, são um formato popular de dados geoespaciais usado em Sistemas de Informações Geográficas (SIG) para representar informações geográficas, como pontos, linhas e polígonos. Esses arquivos são amplamente utilizados para armazenar e compartilhar informações sobre objetos geográficos, como estradas, rios, edifícios, limites administrativos, entre outros.

A estrutura de um shapefile é composta por três arquivos principais com o mesmo nome, mas extensões diferentes:

1. .shp (Shape): Este é o arquivo principal que armazena a geometria dos objetos geográficos (pontos, linhas ou polígonos).

2. .shx (Shape Index): É o arquivo de índice que armazena o índice dos registros do arquivo .shp para permitir um acesso rápido aos dados de geometria.

3. .dbf (dBase File): Este é o arquivo de atributos que armazena os dados associados às geometrias presentes no arquivo .shp. Cada registro no arquivo .dbf corresponde a um objeto geográfico e contém informações adicionais sobre esse objeto.

Para o desenvolvimento de serviços de rota, os shapefiles podem ser utilizados como fonte de dados para representar as estradas, ruas ou outros elementos da rede de transporte. 

## 2. EPSGs e transformações de coordenas

Existem diversos sistemas de referência de coordenadas (SRC) que são utilizados para representar posições geoespaciais no globo terrestre ou em regiões específicas. Cada sistema de referência de coordenadas é projetado para atender a diferentes necessidades de precisão, região geográfica e aplicações específicas. Vou fornecer um resumo sobre alguns dos sistemas de referência de coordenadas mais comuns:

### WGS 84 (EPSG:4326):

* O World Geodetic System 1984 (WGS 84) é um sistema global de referência de coordenadas geodésicas utilizado em todo o mundo.
* É amplamente utilizado em sistemas de mapeamento, serviços de GPS e plataformas de SIG, incluindo o Google Maps e o OpenStreetMap.
* O código EPSG associado é 4326.

### UTM (Universal Transverse Mercator):
* O UTM é um sistema projetado de coordenadas utilizado para representar posições em áreas limitadas, dividindo o mundo em zonas.
* Cada zona UTM tem sua própria projeção transversa de Mercator, adequada para medições precisas em pequenas áreas.
* É frequentemente utilizado em aplicações de cartografia topográfica e para representar posições em áreas locais.
* Cada zona UTM possui um código EPSG específico.

### SIRGAS (Sistema de Referência Geocêntrico para as Américas):

* O SIRGAS é um sistema geocêntrico de referência utilizado na América do Sul.
* Foi criado para fornecer uma base de referência comum para aplicações geodésicas em toda a região.
* O código EPSG associado varia de acordo com o país ou região específica.
SAD69 (South American Datum 1969):

* O SAD69 é um sistema de datum geodésico utilizado na América do Sul, anteriormente amplamente utilizado na região.
* Foi amplamente substituído pelo SIRGAS, mas ainda pode ser encontrado em alguns dados mais antigos.
* O código EPSG associado é 4618.

### NAD83 (North American Datum 1983):

* O NAD83 é um sistema de datum geodésico utilizado na América do Norte, incluindo os Estados Unidos e o Canadá.
* É comumente usado para aplicações de mapeamento, cartografia e sistemas de informações geográficas na América do Norte.
* O código EPSG associado é 4269.

### ETRS89 (European Terrestrial Reference System 1989):

* O ETRS89 é um sistema de referência de coordenadas utilizado na Europa.
* É baseado no WGS 84, mas possui uma rede de pontos de controle fixos para garantir a precisão regional.
* O código EPSG associado é 4258.

## 3. Folium e plots

O Folium utiliza o sistema de coordenadas geográficas WGS 84 (World Geodetic System 1984) como padrão para plotar dados no mapa. O código EPSG associado ao sistema de coordenadas WGS 84 é 4326.

Ao utilizar o Folium para plotar dados geoespaciais em um mapa, você pode fornecer coordenadas no sistema WGS 84, ou seja, as coordenadas de latitude e longitude em graus decimais (EPSG 4326). O Folium se encarrega de projetar essas coordenadas em um mapa que usa a projeção de Mercator, a qual é comumente utilizada para visualização em mapas interativos.

O uso do sistema WGS 84 pelo Folium permite que os dados sejam exibidos corretamente em qualquer região do mundo, possibilitando que você crie mapas interativos com informações precisas e consistentes, independentemente da localização dos seus dados geoespaciais.

## 4. Referências

Geopandas Documentation. Acessado em: https://geopandas.org/. 

Parâmetros de transformação de coordenadas ArcGIS. Acessado em: 
https://forest-gis.com/2015/02/parametros-de-transformacao-de-coordenadas-arcmap.html/#:~:text=Para%20realizar%20uma%20transforma%C3%A7%C3%A3o%20de,ao%20n%C3%ADvel%20de%20poucos%20cent%C3%ADmetros.

## 5. Histórico de versão 
|Nome  | Descrição | Data  |
|---------|---------|---------|
|Luiz Felipe     |   Estudo sobre Shapefiles    | 30/07/2023        |
