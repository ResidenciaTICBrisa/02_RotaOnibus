import requests
import folium

# URL do endpoint do FastAPI
API_URL = "http://127.0.0.1:8000/calculate_route"

# Coordenadas de origem (Você pode alterá-las conforme necessário)
lat_origin = -15.989377
lon_origin = -48.044908

# Definindo as paradas no body da requisição
body = {
    "current_location": {
        "lat": lat_origin,
        "lon": lon_origin
    },
    "paradas": [
        {"lat": -15.987927, "lon": -48.044693},
        {"lat": -15.842100, "lon": -48.045521}
    ]
}

# Fazendo a requisição para a API
response = requests.post(API_URL, json=body)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Coordenadas para baldeação e rota veicular
    baldeacao_coords = data['baldeacao']
    rota_veicular_coords = data['rota_veicular']

    # Criando o mapa com folium centrado na origem
    m = folium.Map(location=[lat_origin, lon_origin], zoom_start=15)

    # Adicionando os caminhos no mapa
    folium.PolyLine(baldeacao_coords, color="red", weight=2.5).add_to(m)  # Baldeação em vermelho
    folium.PolyLine(rota_veicular_coords, color="blue", weight=2.5).add_to(m)  # Rota veicular em azul

    # Salva o mapa em um arquivo HTML e abre no navegador
    m.save("./nosso_route_map.html")
    print("Mapa salvo como 'nosso_route_map.html'. Abra este arquivo em um navegador para ver a rota.")
else:
    print(f"Erro ao chamar a API: {response.text}")
