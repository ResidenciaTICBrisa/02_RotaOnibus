import requests
import folium

# URL do endpoint do FastAPI
API_URL = "http://127.0.0.1:8000/calculate_route"

# Coordenadas de origem (Você pode alterá-las conforme necessário)
lat_origin = -15.989444964529529
lon_origin = -48.044418962814866

lat_destiny = -15.818353856600432
lon_destiny = -47.87465146311891

# Definindo as paradas no body da requisição
body = {
    "current_location": {
        "lat": lat_origin,
        "lon": lon_origin
    },
    "destiny_location": {
        "lat": lat_destiny,
        "lon": lon_destiny
    },
}

# Fazendo a requisição para a API
response = requests.post(API_URL, json=body)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()

    # Coordenadas para baldeação e rota veicular
    baldeacao_coords_orig = data['baldeacao_orig']
    rota_veicular_coords = data['rota_veicular']
    baldeacao_coords_dest = data['baldeacao_dest']
    paradas = data['paradas']

    # Criando o mapa com folium centrado na origem
    m = folium.Map(location=[lat_origin, lon_origin], zoom_start=15)

    # Adicionando os caminhos no mapa
    folium.PolyLine(baldeacao_coords_orig, color="red", weight=2.5).add_to(m)  # Baldeação em vermelho
    folium.PolyLine(rota_veicular_coords, color="blue", weight=2.5).add_to(m)  # Rota veicular em azul
    folium.PolyLine(baldeacao_coords_dest, color="green", weight=2.5).add_to(m)  # Baldeação em verde

    for parada in paradas:
        folium.Marker(
            location=[parada['lat'], parada['lon']],
            popup=f"ID da Parada: {parada['id_stop']}",  # Isso exibirá o ID da parada quando você clicar no marcador
            icon=folium.Icon(color="blue")
        ).add_to(m)

    # Salva o mapa em um arquivo HTML e abre no navegador
    m.save("rota_onibus.html")
    print("Mapa salvo como 'rota_onibus.html'. Abra este arquivo em um navegador para ver a rota.")
else:
    print(f"Erro ao chamar a API: {response.text}")
