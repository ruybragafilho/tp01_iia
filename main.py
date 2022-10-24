#! /usr/bin/env python3


# Comando para executar o programa
#./main.py [caminho para arquivo mapa] [identificador metodo] xi yi xf yf

# Exemplo
# ./main.py mapa_teste.map BFS 1 1 4 3

# Identificadores dos metodos de busca
# BFS - Busca em Largura
# IDS - Aprofundamento Iterativo
# UCS - Busca de Custo Uniforme
# Greedy 
# Astar


import sys
from mapa import Mapa




# Carregar parametros da linha de comando
arquivo_entrada = sys.argv[1]
identificador_metodo = sys.argv[2]

xi = sys.argv[3]
yi = sys.argv[4]
xf = sys.argv[5]
yf = sys.argv[6]


# Caregando o mapa do arquivo
arquivo = open( arquivo_entrada, 'r' )

# Le a largura e a altura do mapa
linhas = arquivo.readlines()
w, h = map(int, (linhas[0]).split())

# Le o mapa
matriz = []
for i in range(1, h+1):
    tmp = linhas[i]
    linha = []
    for j in range(w):
        linha.append( tmp[j] )
    matriz.append( linha )
    

# instanciando um objeto da classe mapa
mapa = Mapa(matriz, w, h)
mapa.mostrar_mapa()

# fechando o arquivo e desalocando o buffer linhas
arquivo.close()
linhas = None




# Fim do programa



print( '\n\n' )