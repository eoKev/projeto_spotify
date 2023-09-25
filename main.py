"""
Projeto Spotify - Análise de Dados e Visualização

Este programa permite ao usuário realizar análises de dados e criar visualizações a partir de um arquivo CSV de dados do Spotify.

Módulos Utilizados:
- pandas: Para leitura e manipulação dos dados CSV.
- matplotlib.pyplot: Para criação de gráficos.
- colorama: Para adicionar cores ao console.

Funcionalidades:
1. Mostrar as 10 músicas mais populares de um ano específico.
2. Mostrar os gêneros mais populares de um ano específico.
3. Mostrar as 10 músicas mais tocadas de um artista.
4. Comparar a popularidade de um artista entre dois anos específicos.
5. Comparar a popularidade entre dois artistas.
6. Mostrar as músicas mais longas de um artista.
7. Mostrar as músicas mais curtas de um artista.
0. Sair do programa.

Autor: [Caio, Felipe Gabriel, Kevin]
Data de Criação: [22/09/2023]
"""


import pandas as pd


import matplotlib.pyplot as plt
from colorama import Fore, Style


df = pd.read_csv('spot.csv')

def mostrar_top10_musicas(ano):
    top10_mais_populares = df[df['year'] == ano].nlargest(10, 'track_popularity')
    if not top10_mais_populares.empty:
        plt.figure(figsize=(10, 6))
        plt.barh(top10_mais_populares['track_name'], top10_mais_populares['track_popularity'], color='skyblue')
        plt.xlabel('Popularidade')
        plt.ylabel('Música')
        plt.title(f'As 10 músicas mais populares de {ano}', color='blue')
        plt.gca().invert_yaxis()
        plt.show()
    else:
        print(f"{Fore.RED}Nenhuma música encontrada para o ano {ano}.{Style.RESET_ALL}")

def mostrar_generos_populares(ano):
    generos_populares = df[df['year'] == ano]['artist_genres'].str.strip("[]").str.split(
        ',').explode().str.strip().value_counts().nlargest(10)
    if not generos_populares.empty:
        plt.figure(figsize=(10, 6))
        generos_populares.plot(kind='bar', color='lightgreen')
        plt.xlabel('Gênero')
        plt.ylabel('Contagem')
        plt.title(f'Gêneros mais populares de {ano}', color='green')
        plt.show()
    else:
        print(f"{Fore.RED}Nenhum gênero encontrado para o ano {ano}.{Style.RESET_ALL}")

def mostrar_musicas_artista(artista):
    musicas_do_artista = df[df['artist_name'] == artista].nlargest(10, 'track_popularity')
    if not musicas_do_artista.empty:
        plt.figure(figsize=(10, 6))
        plt.barh(musicas_do_artista['track_name'], musicas_do_artista['track_popularity'], color='salmon')
        plt.xlabel('Popularidade')
        plt.ylabel('Música')
        plt.title(f'As 10 músicas mais tocadas de {artista}', color='red')
        plt.gca().invert_yaxis()
        plt.show()
    else:
        print(f"{Fore.RED}Nenhuma música encontrada para o artista {artista}.{Style.RESET_ALL}")

def comparar_popularidade_artista(artista, ano1, ano2):
    popularidade_artista_ano1 = df[(df['artist_name'] == artista) & (df['year'] == ano1)]['artist_popularity']
    popularidade_artista_ano2 = df[(df['artist_name'] == artista) & (df['year'] == ano2)]['artist_popularity']
    if not popularidade_artista_ano1.empty and not popularidade_artista_ano2.empty:
        plt.figure(figsize=(6, 4))
        plt.bar([ano1, ano2], [popularidade_artista_ano1.values[0], popularidade_artista_ano2.values[0]], color=['royalblue', 'orange'])
        plt.xlabel('Ano')
        plt.ylabel('Popularidade')
        plt.title(f'Comparação de popularidade de {artista} entre {ano1} e {ano2}', color='purple')
        plt.xticks([ano1, ano2])
        plt.show()
    else:
        print(f"{Fore.RED}Não foi possível encontrar dados de popularidade para {artista} nos anos especificados.{Style.RESET_ALL}")

def comparar_popularidade_artistas(artista1, artista2):
    popularidade_artista1 = df[df['artist_name'] == artista1]['artist_popularity']
    popularidade_artista2 = df[df['artist_name'] == artista2]['artist_popularity']
    if not popularidade_artista1.empty and not popularidade_artista2.empty:
        plt.figure(figsize=(6, 4))
        plt.bar([artista1, artista2], [popularidade_artista1.values[0], popularidade_artista2.values[0]], color=['gold', 'pink'])
        plt.xlabel('Artista')
        plt.ylabel('Popularidade')
        plt.title(f'Comparação de popularidade entre {artista1} e {artista2}', color='brown')
        plt.show()
    else:
        print(f"{Fore.RED}Não foi possível encontrar dados de popularidade para os artistas especificados.{Style.RESET_ALL}")

def listar_musicas_longas_curtas(artista, escolha):
    musicas_artista = df[df['artist_name'] == artista]
    if not musicas_artista.empty:
        if escolha == 'L':
            musicas_longas = musicas_artista.nlargest(10, 'duration_ms')
            titulo = 'Músicas mais longas'
        elif escolha == 'C':
            musicas_longas = musicas_artista.nsmallest(10, 'duration_ms')
            titulo = 'Músicas mais curtas'

        plt.figure(figsize=(12, 6))
        plt.barh(musicas_longas['track_name'], musicas_longas['duration_ms'], color='lightblue')
        plt.xlabel('Duração (ms)')
        plt.ylabel('Música')
        plt.title(f'{titulo} de {artista}', color='blue')
        plt.gca().invert_yaxis()
        plt.show()
    else:
        print(f"{Fore.RED}Não foi possível encontrar dados de músicas para {artista}.{Style.RESET_ALL}")


while True:
    print("\n###############################################")
    print("#                Menu Principal               #")
    print("###############################################")
    print(f"{Fore.YELLOW}1{Style.RESET_ALL} - As 10 músicas mais populares de um ano específico")
    print(f"{Fore.YELLOW}2{Style.RESET_ALL} - Os gêneros mais populares de um ano específico")
    print(f"{Fore.YELLOW}3{Style.RESET_ALL} - As 10 músicas mais tocadas de um artista")
    print(f"{Fore.YELLOW}4{Style.RESET_ALL} - Comparação de popularidade de um artista entre dois anos específicos")
    print(f"{Fore.YELLOW}5{Style.RESET_ALL} - Comparação de popularidade entre dois artistas")
    print(f"{Fore.YELLOW}6{Style.RESET_ALL} - Mostrar as músicas mais longas de um artista")
    print(f"{Fore.YELLOW}7{Style.RESET_ALL} - Mostrar as músicas mais curtas de um artista")
    print(f"{Fore.RED}0{Style.RESET_ALL} - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        ano = int(input("Digite o ano específico: "))
        mostrar_top10_musicas(ano)

    elif escolha == '2':
        ano = int(input("Digite o ano específico: "))
        mostrar_generos_populares(ano)

    elif escolha == '3':
        artista = input("Digite o nome do artista: ")
        mostrar_musicas_artista(artista)

    elif escolha == '4':
        artista = input("Digite o nome do artista: ")
        ano1 = int(input("Digite o primeiro ano: "))
        ano2 = int(input("Digite o segundo ano: "))
        comparar_popularidade_artista(artista, ano1, ano2)

    elif escolha == '5':
        artista1 = input("Digite o nome do primeiro artista: ")
        artista2 = input("Digite o nome do segundo artista: ")
        comparar_popularidade_artistas(artista1, artista2)

    elif escolha == '6':
        artista = input("Digite o nome do artista: ")
        listar_musicas_longas_curtas(artista, 'L')

    elif escolha == '7':
        artista = input("Digite o nome do artista: ")
        listar_musicas_longas_curtas(artista, 'C')

    elif escolha == '0':
        break

    else:
        print(f"{Fore.RED}Opção inválida. Tente novamente.{Style.RESET_ALL}")
