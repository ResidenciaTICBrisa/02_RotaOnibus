# Django e Django REST Framework

## 1. Diferenças entre Django e Django REST Framework

Ambos escritos em **Python**, porém com finalidades diferentes. O Django facilita a construção de sites e aplicações web. Já o Django Rest, é um conjunto de ferramentas poderosas para construir web APIs.

## 2. Django Framework

O propósito do Django está no desenvolvimento de aplicações web e sites. Lançado em Julho de 2005, atualmente, possui uma estrutura com ORM próprio, suporte à virtualização, autenticação e Templates.

Sua principal convenção é o *DRY* (Don't Repeat Yourself, que significa não seja repetitivo), que visa o máximo de proveito do código criado, evitando código duplicado.


### 2.1 Arquitetura Django Framework

O Django utiliza um padrão similar ao MVC model-view-controller, porém, aqui chamado de MTV (model-template-view), onde dividimos a aplicação em camadas ou partes, tornando o código mais organizado e legível.

    M: Model Regras de negócio, como o model do MVC.

    T: Template Arquivo html que será renderizado pela view.

    V: View Equivalente ao controller do MVC.

<!-- [Imagem](Estudos/assets/ArquiteturaDjango.jpeg) -->

## 3. Django REST Framework

O foco aqui é o desenvolvimento de web API's de forma simples e ágil. Segundo a documentação oficial, o Django Rest gera uma [API](#31-api) navegável que auxilia na usabilidade para os desenvolvedores. Além disso, possui um sistema de autenticação e serialização dos dados.

Esse é um dos motivos para usar o Django REST Framework, porque ele torna a [serialização](#32-serialização-e-desserialização-dos-dados) mais fácil. Pense que você está desenvolvendo uma API e o JSON é o tipo principal dos recursos disponibilizados. Transitar os dados JSON para um formato que o Python entenda, e vice-versa, é feito de forma simples com este framework.

O Django Rest funciona como um complemento ao Django, isso significa que é necessária a instalação do Django, e consequentemente, do Rest Framework

### 3.1 API 

Uma Web API (Application Programming Interface) é um conjunto de padrões e protocolos que permite a comunicação entre diferentes sistemas e aplicativos por meio da internet. Ela define um conjunto de regras e métodos que especificam como solicitar e obter dados ou funcionalidades de um determinado serviço ou aplicativo.

Em termos simples, uma Web API permite que diferentes aplicativos se comuniquem e interajam entre si, mesmo que sejam desenvolvidos em plataformas ou linguagens de programação diferentes. Ela funciona como uma interface que expõe recursos e funcionalidades de um sistema, permitindo que outros aplicativos façam solicitações e obtenham respostas estruturadas.

As Web APIs são baseadas em protocolos da web, como HTTP (Hypertext Transfer Protocol), e geralmente seguem os princípios da arquitetura REST (Representational State Transfer). Isso significa que as APIs são projetadas de forma a serem stateless (sem estado) e a utilizar os métodos HTTP (como GET, POST, PUT, DELETE) para realizar operações específicas nos recursos disponibilizados.

Uma Web API pode fornecer uma variedade de recursos e serviços, desde acesso a dados, como consulta de informações em um banco de dados, até funcionalidades mais complexas, como integração com serviços externos, processamento de pagamentos ou envio de mensagens.

As APIs são amplamente utilizadas no desenvolvimento de aplicativos e sistemas modernos, permitindo a integração de diferentes componentes e a construção de soluções mais flexíveis e escaláveis. Elas facilitam a troca de dados e a interoperabilidade entre sistemas, possibilitando a criação de aplicativos mais poderosos e interconectados.

### 3.2 Serialização e desserialização dos dados

No contexto de desenvolvimento de APIs, serialização e desserialização referem-se aos processos de transformação de dados em um formato específico para transmissão ou armazenamento e, em seguida, a reconstrução desses dados a partir desse formato.

A serialização é o processo de converter objetos ou estruturas de dados em um formato adequado para ser transmitido ou armazenado. Isso é necessário porque as APIs geralmente se comunicam com diferentes sistemas ou aplicativos, e cada um pode ter seu próprio formato de dados preferido. A serialização permite que os dados sejam convertidos em um formato comum e compreensível por ambas as partes. Durante a serialização, os dados são convertidos em uma sequência de bytes que podem ser transmitidos pela rede ou armazenados em um arquivo.

Por outro lado, a desserialização é o processo inverso. Envolve a reconstrução dos dados a partir do formato serializado de volta ao formato original do objeto ou estrutura de dados. A desserialização é necessária para que os dados transmitidos ou armazenados possam ser interpretados corretamente pelo destinatário ou pela aplicação que os recebe. Durante a desserialização, os bytes recebidos são convertidos de volta em objetos ou estruturas de dados utilizáveis.

Em resumo, a serialização e a desserialização são operações complementares que permitem a transmissão ou armazenamento de dados em um formato comum. A serialização converte os dados em uma sequência de bytes para transmissão ou armazenamento, enquanto a desserialização reconstrói esses dados a partir da sequência de bytes, permitindo que eles sejam interpretados e usados pela aplicação receptor ou pela API.

## 4. Referências

- [1] [Documentação Django](https://www.django-rest-framework.org/#:~:text=Django%20REST%20framework%20is%20a,toolkit%20for%20building%20Web%20APIs.&text=The%20Web%20browsable%20API%20is,and%20non%2DORM%20data%20sources.)
- [2] [Documentação Django Rest](https://www.django-rest-framework.org/#:~:text=Django%20REST%20framework%20is%20a,toolkit%20for%20building%20Web%20APIs.&text=The%20Web%20browsable%20API%20is,and%20non%2DORM%20data%20sources.)
- [3] [Django Girls Blog](https://tutorial.djangogirls.org/en/)
- [4] [Tutorial Youtube Django Rest Framework](https://www.youtube.com/watch?v=gFsIGJR5R8I)
- [5] [Serialização e desserialização dos dados](https://cursos.alura.com.br/forum/topico-serializacao-e-desserializacao-110845?_gl=1*s0eokq*_ga*MTM4Mjk1ODE5NC4xNjc5NTkyODMw*_ga_59FP0KYKSM*MTY4Nzk1NzI4Ny41LjEuMTY4Nzk1NzMwNS40Mi4wLjA.*_fplc*Rm95ZWRwQnZWJTJCU09pQjA4ZUJaeWxlUlZsQUlKZDZyTDZDS0pBQU9rdTIyODBTNGY4UXBUbiUyRjRvbktvRzVIbyUyRll0ZHBJZGVPR0FRdW43RHFiNXF3TkQydTJDU1h5ekF0OWZaUXRBbzclMkZiN09UbXJEb1BPMkEyRDdwa3ZpTHclM0QlM0Q.)


## 5. Histórico de Versão

| Versão | Alteração |  Responsável  | Revisor | Data  |
| ------ | :-------: | :-----------: | :-----: | :---: |
|  1.0   | Criando dos tópicos 1, 2, 3 e 4 | Leonardo Vitoriano |  -   | 28/06/23 |
