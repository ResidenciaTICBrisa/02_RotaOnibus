import requests
import folium

# URL do endpoint do FastAPI
API_URL = "http://127.0.0.1:8000/calculate_route"

# Coordenadas de origem (Você pode alterá-las conforme necessário)
lat_origin = -15.998180
lon_origin = -48.055908

# Fazendo a requisição para a API
response = requests.post(
    API_URL, json={"lat_origin": lat_origin, "lon_origin": lon_origin})

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    data = response.json()
    route_coords = data['baldeacao']

    # Criando o mapa com folium centrado na origem
    m = folium.Map(location=[lat_origin, lon_origin], zoom_start=15)

    # Adicionando o caminho no mapa
    folium.PolyLine(route_coords, color="blue", weight=2.5).add_to(m)

    # Salva o mapa em um arquivo HTML e abre no navegador
    m.save("./nosso_route_map.html")
    print("Mapa salvo como 'route_map.html'. Abra este arquivo em um navegador para ver a rota.")
else:
    print(f"Erro ao chamar a API: {response.text}")
