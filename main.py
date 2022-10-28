#! /usr/bin/env python3


# Comando para executar o programa
#./main.py [caminho para arquivo mapa] [identificador metodo] xi yi xf yf

# Exemplo
# ./main.py mapa_teste.map BFS 1 1 3 1

# Identificadores dos metodos de busca
# BFS - Busca em Largura
# IDS - Aprofundamento Iterativo
# UCS - Busca de Custo Uniforme
# Greedy 
# Astar


import sys
from mapa import Mapa
from bfs import BFS




# Carregar parametros da linha de comando
arquivo_entrada = sys.argv[1]
identificador_metodo = sys.argv[2]

xi = int(sys.argv[3])
yi = int(sys.argv[4])
xf = int(sys.argv[5])
yf = int(sys.argv[6])


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

# fechando o arquivo e desalocando o buffer linhas
arquivo.close()
linhas = None


posicao_inicial = (xi, yi)
posicao_final = (xf, yf)

if( identificador_metodo == 'BFS' ):
    busca = BFS(mapa)
    resultado = busca.pathfinder( posicao_inicial, posicao_final )
elif( identificador_metodo == 'IDS' ):
    print( '\nIDS\n' )
elif( identificador_metodo == 'UCS' ):
    print( '\nUCS\n' )
elif( identificador_metodo == 'Greedy' ):
    print( '\nGreedy\n' )
elif( identificador_metodo == 'Astar' ):
    print( '\nAstar\n' )
else:
    print( '\nMetodo Invalido\n' )
    exit()



if( resultado ):
    busca.get_path( posicao_inicial, posicao_final )
    print( busca.get_path_cost(), ' ', end='' )
    for i in busca.path:
        print( i, ' ', end='' )
else:
    print('Caminho nao encontrado')

# Fim do programa
