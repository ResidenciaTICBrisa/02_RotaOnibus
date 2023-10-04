# Construção do Grafo

## 1. Notebook 

O notebook para a Construção do Grafo, usando a biblioteca Networkx, encontra-se no link a seguir:

- [Notebook construção do grafo](/docs/Notebooks/PreProcessamento/LinhaOnibus-Grafo.ipynb)

## 2. DataFrames

A base para a construção dos Grafos são os DataFrames, que possuem todas as paradas, com seus respectivos dados: identificador, latitude e longitude, em ordem da rota do ônibus. A partir desse DataFrame de todas as paradas do Distrito Federal, é possível identificar quatro tipos de linhas de ônibus com base na coluna 'SENTIDO': linhas ida e volta, linhas somente ida, linhas somente volta e linhas circulares. Essa separação faz-se necessário pois existirá uma função de Contrução do Grafo diferente para os dois grupos de linhas a seguir: 

1. Linhas Ida e Volta, e Linhas Circulares; e
2. Linhas somente Ida e somente Volta;

Dito isso, um snippet do código que gera os DataFrames necessários, encontra-se a seguir:


        # Carregar o DataFrame salvo anteriormente
        df_linhas_e_paradas = pd.read_csv('linhas_e_paradasID_ordenadas_sentido.csv', converters={'Paradas': ast.literal_eval}) 

        ida_df = df_linhas_e_paradas[df_linhas_e_paradas['Sentido']=='IDA']
        volta_df = df_linhas_e_paradas[df_linhas_e_paradas['Sentido']=='VOLTA']
        linhas_circular = df_linhas_e_paradas[df_linhas_e_paradas['Sentido']=='CIRCULAR']

        # Junta os DataFrames da 'IDA' e 'VOLTA' usando o número da linha como chave
        merged_df = ida_df.merge(volta_df, on='Linha')

        # Coluna 'Paradas_x' que contém a união das paradas da IDA e da VOLTA
        for idx, row in merged_df.iterrows():
            row['Paradas_x'].extend(row['Paradas_y'])

        # Mantém apenas as colunas relevantes
        merged_df = merged_df[['Linha', 'Paradas_x']]
        merged_df = merged_df.rename(columns={'Paradas_x': 'Paradas'})

        # Identifica as linhas de ônibus presentes apenas na IDA
        linhas_somente_ida = ida_df[~ida_df['Linha'].isin(volta_df['Linha'])]

        # Identifica as linhas de ônibus presentes apenas na VOLTA
        linhas_somente_volta = volta_df[~volta_df['Linha'].isin(ida_df['Linha'])]

        # Identifica as linhas IDA+VOLTA e Circulares
        linhas_conectadas = pd.concat([merged_df, linhas_circular])

        # Identifica linhas somente de IDA e de Volta
        linhas_unicas = pd.concat([linhas_somente_ida, linhas_somente_volta])

        # Identifica todas as linhas existestes
        linhas_completas_df = pd.concat([linhas_conectadas, linhas_unicas])

## 3. Criação do Grafo

Após a geração dos DataFrames, e seguindo o artefato de [psudocódigo para a construção do Grafo](/docs/Estudos/PseudoCodigo_RotasGrafos.md), foi possível criar uma instacia de Grafo Direcional, com networkx, e ir adicionando os nós (paradas de ônibus, com latitude e longitude) e arestas (conexão entre os nós, com distancia e linha de ônibus que passam pela aresta). O código resultante é o apresentado a seguir:

        # Criar um grafo Direcional
        GrafoDirecional = nx.DiGraph()

        def geraDataFrameParadas(row):
            # Convertendo a string para uma lista de tuplas
            paradasDaLinha = row['Paradas']

            # Criar um GeoDataFrame temporário
            gdf_temp = gpd.GeoDataFrame(
                {'geometry': [Point(xy) for xy, _ in paradasDaLinha]},
                crs="EPSG:31983"  # Substitua pelo CRS apropriado se for diferente
            )

            # Adicionar coluna dos identificadores das paradas
            gdf_temp['idParada'] = [id for xy, id in paradasDaLinha]

            ## Reprojetar para WGS 84
            gdf_temp = gdf_temp.to_crs(epsg=4326)

            return gdf_temp


        # Função para calcular a distância euclidiana entre dois pontos
        def distance_between_points(origem, destino):
            return geodesic(origem, destino).km


        def adicionaArestaNoGrafo(idNoOrigem, idNoDestino, linha):
            global GrafoDirecional

            # Nós iguais no mesmo Data Frame
            if idNoOrigem == idNoDestino:
                return
                
            origem_coords = (GrafoDirecional.nodes[idNoOrigem]['coords'].y, GrafoDirecional.nodes[idNoOrigem]['coords'].x) 
            destino_coords = (GrafoDirecional.nodes[idNoDestino]['coords'].y, GrafoDirecional.nodes[idNoDestino]['coords'].x)
            # Calcular a distância entre as paradas
            distancia = distance_between_points(origem_coords, destino_coords)
            
            if GrafoDirecional.has_edge(idNoOrigem, idNoDestino):
                data = GrafoDirecional.get_edge_data(idNoOrigem, idNoDestino)
                if linha not in data['linha']: 
                    data['linha'].append(linha)
            else:
                # Adicionar aresta orientada
                GrafoDirecional.add_edge(idNoOrigem, idNoDestino, dist=distancia, linha=[linha])


        def integraParadasDaLinhaNoGrafo(paradas_df, linha):
            global GrafoDirecional

            tamanho_df = len(paradas_df)
            if (not tamanho_df > 0):
                return

            for idx, row in paradas_df.iterrows():
                if row['idParada'] not in GrafoDirecional:
                    GrafoDirecional.add_node(row['idParada'], coords=row['geometry'])
                if idx > 0:
                    origem = paradas_df.iloc[(idx-1)]['idParada']
                    destino = paradas_df.iloc[idx]['idParada']
                    adicionaArestaNoGrafo(origem, destino, linha)


        def integraParadasDaLinhaNoGrafoConectado(paradas_df, linha):
            global GrafoDirecional

            tamanho_df = len(paradas_df)
            if (not tamanho_df > 0):
                return
            
            for idx, row in paradas_df.iterrows():
                if row['idParada'] not in GrafoDirecional:
                    GrafoDirecional.add_node(row['idParada'], coords=row['geometry'])
                if idx > 0:
                    origem = paradas_df.iloc[(idx-1)]['idParada']
                    destino = paradas_df.iloc[idx]['idParada']
                    adicionaArestaNoGrafo(origem, destino, linha)
            primeiro_no = paradas_df['idParada'].iloc[0]
            ultimo_no = paradas_df['idParada'].iloc[tamanho_df-1]
            adicionaArestaNoGrafo(ultimo_no, primeiro_no, linha)
            
        # Percorrendo todas as linhas de ônibus de IDA+VOLTA e circulares
        for idx, row in linhas_conectadas.iterrows():
            paradas_df = geraDataFrameParadas(row)
            linha = str(row['Linha'])
            integraParadasDaLinhaNoGrafoConectado(paradas_df, linha)

        # Percorrendo todas as linhas de ônibus de somente IDA e somente VOLTA 
        for idx, row in linhas_unicas.iterrows():
            paradas_df = geraDataFrameParadas(row)
            linha = str(row['Linha'])
            integraParadasDaLinhaNoGrafo(paradas_df, linha)

## 4. Salvando o Grafo

Depois de gerado o Grafo, é possível salvá-lo estaticamente para carregar e usar quando necessário. É possível armazená-lo de vaŕias formas, e a escolhida foi dentre elas foi com a biblioteca Pickle, que gera um arquivo com extensão '.grafo'. O código é mostrado a baixo:

        import pickle

        # Salvar o grafo em um arquivo usando pickle
        with open('grafoDirecional.grafo', 'wb') as f:
            pickle.dump(GrafoDirecional, f)

## 5. Conclusão e Próximos Passos

Dessa forma, foi possível desenvolver um Grafo Direcionado Estático de todas as linhas de ônibus e suas respectivas paradas, no Distrito Federal (DF). Nos próximos passos, a equipe almeja usufruir do Grafo para desenhar e implementar algoritmos de rota ótima, que possuem como resultado: uma rota, que possui a menor quantidade de ônibus, quais são eles e quais as paradas, que levam o usuário da origem até o destino.

## 6. Referências

- [Networkx](https://networkx.org/documentation/stable/auto_examples/geospatial/plot_osmnx.html)

## 7. Histórico de Versão

| Versão | Alteração | Responsável | Revisor | Data  |
| :----: | :-------: | :---------: | :-----: | :---: | 
| 1.0    | Criando do documento | Leonardo Vitoriano | - | 04/10 |