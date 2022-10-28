# Módulo que implementa o algoritmo de busca aprofundamento iterativo - IDS
# Autor: Ruy Braga Filho


from collections import deque
from pathfinder import Pathfinder
from mapa import Mapa


class IDS( Pathfinder ):


    def __init__( self, mapa ):

        super().__init__(mapa)



    # Metodo que implementa o algoritmo de busca BFS
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
        
            # Explora o primeiro elemento da open list
            (x,y) = self.open_list.popleft()  
            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['expandida']

            # verifica se a posicao de cima eh o goal. 
            # Se for, encerra busca. Se nao for, a insere 
            # na open list
            (xs, ys) = self.mapa.sobe(x,y)            
            self.inserir_posicao_na_open_list( xs, ys, x, y )
            if( (xs, ys) == posicao_final ):
                return True            

            # verifica se a posicao de baixo eh o goal. 
            # Se for, encerra busca. Se nao for, a insere 
            # na open list
            (xi, yi) = self.mapa.desce(x,y)
            self.inserir_posicao_na_open_list( xi, yi, x, y )            
            if( (xi, yi) == posicao_final ):
                return True                       

            # verifica se a posicao aa esquerda eh o goal. 
            # Se for, encerra busca. Se nao for, a insere 
            # na open list
            (xe, ye) = self.mapa.esquerda(x,y)
            self.inserir_posicao_na_open_list( xe, ye, x, y )  
            if( (xe, ye) == posicao_final ):
                return True                        
            
            # verifica se a posicao aa direita eh o goal. 
            # Se for, encerra busca. Se nao for, a insere 
            # na open list
            (xd, yd) = self.mapa.direita(x,y)
            self.inserir_posicao_na_open_list( xd, yd, x, y )  
            if( (xd, yd) == posicao_final ):
                return True   


            
