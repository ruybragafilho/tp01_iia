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

print( '\n\n' )


(x, y) = mapa.sobe(0, 0)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.sobe(0, 1)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.sobe(1, 1)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.desce(4, 2)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.desce(3, 1)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.esquerda(0, 0)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.esquerda(1, 1)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.esquerda(2, 2)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.direita(4, 2)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.esquerda(3, 2)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )


(x, y) = mapa.esquerda(1, 2)
print( 'x e y', x, y )
if( mapa.posicao_eh_valida(x, y) ):
    print( mapa.custo(x, y) )
else:
    print( 'Posicao invalida' )



# Fim do programa



print( '\n\n' )