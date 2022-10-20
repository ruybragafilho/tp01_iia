#! /usr/bin/env python3

import sys




#mapa = []
#w = 0
#h = 0





# ./pathfinder.py mapa_teste.map BFS xi yi xf yf
# BFS - Busca em Largura
# IDS - Aprofundamento Iterativo
# UCS - Busca de Custo Uniforme
# Greedy 
# Astar

# Carregar parametros
arquivo_entrada = sys.argv[1]
identificador_metodo = sys.argv[2]

xi = sys.argv[3]
yi = sys.argv[4]
xf = sys.argv[5]
yf = sys.argv[6]



# Imprimir parametros
print( '\n\n' )

print( 'arquivo_entrada: ', arquivo_entrada )
print( 'identificador_metodo: ', identificador_metodo )

print( '\nxi: ', xi )
print( 'yi: ', yi )
print( 'xf: ', xf )
print( 'yf: ', yf )

print( '\nNumero grande: ', 2.0**32 )

print( '\n\n' )



# Caregando o mapa do arquivo
arquivo = open( arquivo_entrada, 'r' )

# Le a largura e a altura do mapa
linhas = arquivo.readlines()
w, h = map(int, (linhas[0]).split())
print( 'w: ', w )
print( 'h: ', h )

# Le as outras linhas do mapa
for linha in linhas:
    print(linha)


print( '\n\n' )