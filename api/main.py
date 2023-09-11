from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Coordinates(BaseModel):
    lat_origin: float
    lon_origin: float
    lat_destination: float
    lon_destination: float


@app.get('/', tags=['Root'], summary='Verifica se o servidor está rodando')
async def root():
    return {'Servidor rodando!'}

@app.post('/paradas/',
          tags=['Paradas'],
          summary='Calcula e retorna as paradas ao longo do caminho',
          description='''Este endpoint aceita coordenadas de origem e destino e retorna as paradas necessárias para a realização do trajeto.  
          - `lat_origin`: Latitude da origem (entre -90 e 90)  
          - `lon_origin`: Longitude da origem (entre -180 e 180)  
          - `lat_destination`: Latitude do destino (entre -90 e 90)  
          - `lon_destination`: Longitude do destino (entre -180 e 180)'''
          )
async def get_coordinates(coordinates: Coordinates):
    if not (-90 <= coordinates.lat_origin <= 90):
        raise HTTPException(
            status_code=400, detail="Latitude de origem inválida. Deve ser entre -90 e 90.")

    if not (-180 <= coordinates.lon_origin <= 180):
        raise HTTPException(
            status_code=400, detail="Longitude de origem inválida. Deve ser entre -180 e 180.")

    if not (-90 <= coordinates.lat_destination <= 90):
        raise HTTPException(
            status_code=400, detail="Latitude de destino inválida. Deve ser entre -90 e 90.")

    if not (-180 <= coordinates.lon_destination <= 180):
        raise HTTPException(
            status_code=400, detail="Longitude de destino inválida. Deve ser entre -180 e 180.")

    # Simulação de paradas como uma lista de dicionários
    paradas = [
        {'nome': 'Parada 1', 'coordenadas': [40.712776, -74.005974]},
        {'nome': 'Parada 2', 'coordenadas': [34.052235, -118.243683]},
        {'nome': 'Parada 3', 'coordenadas': [41.878113, -87.629799]},
        {'nome': 'Parada 4', 'coordenadas': [42.878113, -88.629799]},
        {'nome': 'Parada 5', 'coordenadas': [43.878113, -89.629799]},
        {'nome': 'Parada 6', 'coordenadas': [44.878113, -90.629799]},

        # Adicione mais paradas conforme necessário
    ]

    return {'origin': [coordinates.lat_origin, coordinates.lon_origin],
            'destination': [coordinates.lat_destination, coordinates.lon_destination],
            'paradas': paradas}