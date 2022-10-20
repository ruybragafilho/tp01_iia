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



# Imprimir parametros
print( '\n\n' )

print( 'arquivo_entrada: ', arquivo_entrada )
print( 'identificador_metodo: ', identificador_metodo )

print( '\nxi: ', xi )
print( 'yi: ', yi )
print( 'xf: ', xf )
print( 'yf: ', yf )


print( '\n\n' )



# Caregando o mapa do arquivo
arquivo = open( arquivo_entrada, 'r' )

# Le a largura e a altura do mapa
linhas = arquivo.readlines()
w, h = map(int, (linhas[0]).split())
print( 'w: ', w )
print( 'h: ', h )


matriz = []
# Le as outras linhas do mapa
for i in range(1, h+1):
    tmp = linhas[i]
    linha = []
    for j in range(w):
        linha.append( tmp[j] )
    matriz.append( linha )
    
print( matriz )




# instanciando um objeto da classe mapa
mapa = Mapa(matriz, w, h)
mapa.mostrar_mapa()


retorno = mapa.sobe(0, 0)
print( 'Retorno sobe (0,0): ', retorno)

retorno = mapa.sobe(0, 1)
print( 'Retorno sobe (0,1): ', retorno)

retorno = mapa.sobe(1, 1)
print( 'Retorno sobe (1,1): ', retorno)


retorno = mapa.desce(4, 2)
print( '\nRetorno desce (4,2): ', retorno)

retorno = mapa.desce(3, 1)
print( 'Retorno desce (3,1): ', retorno)


retorno = mapa.esquerda(0, 0)
print( '\nRetorno esquerda (0,0): ', retorno)

retorno = mapa.esquerda(1, 1)
print( 'Retorno esquerda (1,1): ', retorno)

retorno = mapa.esquerda(2, 2)
print( 'Retorno esquerda (2,2): ', retorno)


retorno = mapa.direita(4, 2)
print( '\nRetorno direita (4,2): ', retorno)

retorno = mapa.direita(3, 2)
print( 'Retorno direita (3,2): ', retorno)

retorno = mapa.direita(1, 2)
print( 'Retorno direita (1,2): ', retorno)



# Fim do programa



print( '\n\n' )