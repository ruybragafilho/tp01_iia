# Módulo que implementa o algoritmo de busca aprofundamento iterativo - IDS
# Autor: Ruy Braga Filho


from collections import deque
from pathfinder import Pathfinder
from mapa import Mapa


class IDS( Pathfinder ):


    def __init__( self, mapa ):

        super().__init__(mapa)
        self.open_list = deque()        


    # Metodo que insere a posicao (x,y) na open list e registra
    # as coordenadas do seu antecessor na matriz de antecessor 
    def inserir_posicao_na_open_list( self, x, y, x_antecessor, y_antecessor ):  

        if( self.mapa.posicao_eh_valida( x, y ) and 
            self.posicao_nao_foi_visitada( x, y ) ):     

            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['open_list']
            self.open_list.append( (x,y) )

            self.matriz_de_antecessores[y][x] = (y_antecessor, x_antecessor)


    # Metodo que implementa o algoritmo de busca IDS
    def search( self, posicao_inicial, posicao_final ):
        
        # Testa se as posicoes sao validas
        (xi, yi) = posicao_inicial
        (xf, yf) = posicao_final
        if( not(self.mapa.posicao_eh_valida(xi, yi)) or 
            not(self.mapa.posicao_eh_valida(xf, yf)) ):
            return False

        # Testa se a posicao inicial eh o goal
        if( posicao_inicial == posicao_final ):
            return True

        # Se o goal nao for a posicao inicial, inicia a busca
        self.criar_matriz_status_visita()
        self.criar_matriz_de_antecessores()

        (x,y) = posicao_inicial
        self.inserir_posicao_na_open_list( x, y, -1 , -1 )
                
        while( True ):

            # Verifica se a busca eh inviavel
            if( len(self.open_list) == 0 ):
                return False
        
            # Expande o primeiro elemento da open list e verifica se ele 
            # eh o goal. Se for, encerra busca. Se nao for, insere os
            # vizinhos na open list
            (x,y) = self.open_list.pop()  
            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['expandida']
            if( (x, y) == posicao_final ):
                return True                        

            # Insere o vizinho de cima na open list
            (xs, ys) = self.mapa.sobe(x,y)            
            self.inserir_posicao_na_open_list( xs, ys, x, y )

            # Insere o vizinho de baixo na open list
            (xi, yi) = self.mapa.desce(x,y)
            self.inserir_posicao_na_open_list( xi, yi, x, y )            

            # Insere o vizinho da esquerda na open list
            (xe, ye) = self.mapa.esquerda(x,y)
            self.inserir_posicao_na_open_list( xe, ye, x, y )  
            
            # Insere o vizinho da direita na open list
            (xd, yd) = self.mapa.direita(x,y)
            self.inserir_posicao_na_open_list( xd, yd, x, y )  
            
