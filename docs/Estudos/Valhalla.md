# O que é o Valhalla

Valhalla é um sistema de roteamento de código aberto desenvolvido pela Mapzen, que permite calcular rotas entre diferentes pontos em um mapa. Ele oferece uma ampla gama de recursos e pode ser utilizado para construir aplicativos de planejamento de rotas personalizados.

O Valhalla possui uma arquitetura modular que permite que você escolha as partes específicas do sistema que deseja utilizar. Ele oferece suporte a diferentes modos de transporte, como carro, bicicleta, a pé e transporte público. Além disso, também possui recursos avançados, como cálculo de rotas com várias paradas, otimização de rotas, roteamento baseado em preferências, entre outros.

Para utilizar os recursos do Valhalla em uma aplicação de planejamento de rotas,existem algumas ferramentas que podem auxiliar, são elas:

1. Valhalla Core: É a biblioteca principal do Valhalla, escrita em C++, que contém os algoritmos de roteamento e os componentes centrais do sistema. Você pode integrar essa biblioteca ao seu aplicativo para realizar os cálculos de rotas.

2. Valhalla.js: É uma biblioteca JavaScript que permite acessar os recursos do Valhalla em um ambiente de navegador ou servidor. Ela fornece uma interface de programação de aplicativo (API) para enviar solicitações de roteamento e receber respostas em formato JSON.

3. OpenStreetMap (OSM): O Valhalla utiliza os dados do OSM como base para o cálculo das rotas. Portanto, você precisará importar os dados do OSM relevantes para a região em que deseja utilizar o Valhalla.

4. Mapbox: Embora o Valhalla seja independente do Mapbox, você pode usar a plataforma Mapbox para visualizar e renderizar os resultados do roteamento gerados pelo Valhalla. O Mapbox fornece uma série de bibliotecas e ferramentas para trabalhar com mapas interativos.
