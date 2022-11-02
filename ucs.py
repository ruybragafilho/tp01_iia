# Módulo que implementa o algoritmo de busca Dijkstra - UCS (Busca de Custo Uniforme)
# Autor: Ruy Braga Filho


import heapq
from pathfinder import Pathfinder


class UCS( Pathfinder ):


    def __init__( self, mapa ):

        super().__init__(mapa)
        self.open_list = []       

        self.matriz_menor_custo_caminho = []
        self.criar_matriz( self.matriz_menor_custo_caminho, 0.0 )

        self.posicao_inicial = (0,0)
        self.posicao_final = (0,0)


    # Metodo que insere a posicao (x,y) na open list e registra
    # as coordenadas do seu antecessor na matriz de antecessor 
    def inserir_posicao_na_open_list( self, x, y, x_antecessor, y_antecessor, custo_caminho_antecessor ):  

        if( self.mapa.posicao_eh_valida( x, y ) and 
            not self.posicao_expandida( x, y ) ):     

            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['open_list']

            custo_posicao_atual = self.mapa.custo(x, y)
            custo_caminho_atual = custo_caminho_antecessor + custo_posicao_atual
            
            if( self.matriz_menor_custo_caminho[y][x] == 0.0  or  custo_caminho_atual < self.matriz_menor_custo_caminho[y][x] ):
                self.matriz_menor_custo_caminho[y][x] = custo_caminho_atual

            heapq.heappush( self.open_list, ( custo_caminho_atual, (x,y)) )           

            self.matriz_de_antecessores[y][x] = (y_antecessor, x_antecessor)


    # Metodo que retorna o custo do caminho encontrado pelo algoritmo de busca
    def get_path_cost( self ):

        (xi,yi) = self.posicao_inicial
        (xf,yf) = self.posicao_final
        self.path_cost = self.matriz_menor_custo_caminho[yf][xf] - self.mapa.custo(xi,yi)
        return self.path_cost


    # Metodo que implementa o algoritmo de busca UCS (Dijkstra)
    def search( self, posicao_inicial, posicao_final ):

        self.posicao_inicial = posicao_inicial
        self.posicao_final = posicao_final
        
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

        self.inserir_posicao_na_open_list( xi, yi, -1 , -1, 0.0 )
                
        while( True ):

            # Verifica se a busca eh inviavel
            if( len(self.open_list) == 0 ):
                return False
        
            # Expande o primeiro elemento da open list e verifica se ele 
            # eh o goal. Se for, encerra busca. Se nao for, insere os
            # vizinhos na open list
            ( custo_caminho_atual, (x,y) ) = heapq.heappop( self.open_list )
            if( self.matriz_status_visita[y][x] != Pathfinder.status_posicao['expandida'] ):

                self.matriz_status_visita[y][x] = Pathfinder.status_posicao['expandida']
                if( (x, y) == posicao_final ):
                    return True            
    
                # Insere o vizinho de cima na open list
                (xs, ys) = self.mapa.sobe(x,y)            
                self.inserir_posicao_na_open_list( xs, ys, x, y, custo_caminho_atual )
    
                # Insere o vizinho de baixo na open list
                (xi, yi) = self.mapa.desce(x,y)
                self.inserir_posicao_na_open_list( xi, yi, x, y, custo_caminho_atual )            
    
                # Insere o vizinho da esquerda na open list
                (xe, ye) = self.mapa.esquerda(x,y)
                self.inserir_posicao_na_open_list( xe, ye, x, y, custo_caminho_atual )  
                
                # Insere o vizinho da direita na open list
                (xd, yd) = self.mapa.direita(x,y)
                self.inserir_posicao_na_open_list( xd, yd, x, y, custo_caminho_atual )  

            


            
