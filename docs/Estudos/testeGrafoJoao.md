# Análise do funcionamento das Rotas e sua visualização

## Introdução

O primeiro passo é importar as bibliotecas necessárias e realizar a leitura do arquivo com as paradas

```python
# bibiliotecas
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import contextily as cx
import networkx as nx
from shapely.geometry import box, Point, LineString, Polygon, MultiPolygon
from shapely.wkt import loads
import folium

# leitura dos arquivos
pontodeonibus= gpd.read_file('data/paradas.shp')
linhas = gpd.read_file('data/Linhas.shp')
```

Depois indetificamos o sistema de coordenadas utilizado 

```python
pontodeonibus.crs
```

Que nos retorna:

```python
<Projected CRS: EPSG:31983>
Name: SIRGAS 2000 / UTM zone 23S
Axis Info [cartesian]:
- E[east]: Easting (metre)
- N[north]: Northing (metre)
Area of Use:
- name: Brazil - between 48°W and 42°W, northern and southern hemispheres, onshore and offshore.
- bounds: (-48.0, -33.5, -42.0, 5.13)
Coordinate Operation:
- name: UTM zone 23S
- method: Transverse Mercator
Datum: Sistema de Referencia Geocentrico para las AmericaS 2000
- Ellipsoid: GRS 1980
- Prime Meridian: Greenwich
```

Após isso fazemos a conversão dos dois arquivos para o sistema usado no Folium

```python
# Convertendo, paradas de onibus, de Sistema de coordenadas EPSG:31983 para EPSG:4326
parada = pontodeonibus.to_crs("EPSG:4326")
# Convertendo, linhas de onibus, de Sistema de coordenadas EPSG:31983 para EPSG:4326
rota = linhas.to_crs("EPSG:4326")
```

## Plotando mapa das Rotas

```python
# Gera o mapa da região
mapa = folium.Map(location=list(reversed([-47.976167,-15.922460])), tiles="cartodbpositron", zoom_start = 11)

# Obter o objeto a partir da coluna
fga_volta = linestringFGA.geometry.iloc[0]
fga_ida = linestringFGA.geometry.iloc[1]

# Colocando as coordenadas no formato usado pelo folium (latitude, longitude)
coord_ida = [(lat1, lon1) for lon1,lat1 in fga_ida.coords]
coord_volta = [(lat2, lon2) for lon2,lat2 in fga_volta.coords]

# Plotando a ida
folium.PolyLine(locations = coord_ida, color = 'green', tooltip = linestringFGA['linha'].iloc[1]+ ' ' + linestringFGA['sentido'].iloc[1]).add_to(mapa)

#Plotando a volta
folium.PolyLine(locations = coord_volta, color = 'red', tooltip = linestringFGA['linha'].iloc[0]+ ' ' + linestringFGA['sentido'].iloc[0]).add_to(mapa)
```

## Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criando arquivo | João Leles | - | 11/08 |