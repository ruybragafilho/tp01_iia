# Módulo que implementa o algoritmo de busca aprofundamento iterativo - IDS
# Autor: Ruy Braga Filho


from collections import deque
from pathfinder import Pathfinder
from mapa import Mapa


class IDS( Pathfinder ):


    def __init__( self, mapa ):

        super().__init__(mapa)
        self.open_list = deque()


    # Metodo que reinicializa as variaveis auxiliares 
    # usadas pelo busca em profundidade iterativo
    def reset_variaveis_auxiliares( self ):

        self.open_list = deque() 

        numLinhas = self.mapa.get_num_linhas()
        numColunas = self.mapa.get_num_colunas()        
        
        for i in range(numLinhas):
            for j in range(numColunas):
                self.matriz_status_visita[i][j] = Pathfinder.status_posicao['posicao_virgem']
                self.matriz_de_antecessores[i][j] = Pathfinder.antecessor_vazio
            


    # Metodo que insere a posicao (x,y) na open list e registra
    # as coordenadas do seu antecessor na matriz de antecessor 
    def inserir_posicao_na_open_list( self, x, y, x_antecessor, y_antecessor, profundidade ):  

        if( self.mapa.posicao_eh_valida( x, y ) and 
            self.posicao_nao_foi_visitada( x, y ) ):     

            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['open_list']
            self.open_list.append( (profundidade, (x,y)) )

            self.matriz_de_antecessores[y][x] = (y_antecessor, x_antecessor)


    # Metodo que implementa o algoritmo de busca IDS
    def deapLimitedSearch( self, posicao_inicial, posicao_final, profundidade_maxima ):
        
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

        profundidade = 0  
        (x,y) = posicao_inicial
        self.inserir_posicao_na_open_list( x, y, -1 , -1, profundidade )
                
        while( True ):

            # Verifica se a busca eh inviavel
            if( len(self.open_list) == 0 ):
                return False
        
            # Expande o primeiro elemento da open list e verifica se ele 
            # eh o goal. Se for, encerra busca. Se nao for, insere os
            # vizinhos na open list
            (profundidade, (x,y)) = self.open_list.pop()  
            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['expandida']
            if( (x, y) == posicao_final ):
                return True                        
            profundidade += 1

            if( profundidade <= profundidade_maxima ):

                # Insere o vizinho de cima na open list
                (xs, ys) = self.mapa.sobe(x,y)            
                self.inserir_posicao_na_open_list( xs, ys, x, y, profundidade )
    
                # Insere o vizinho de baixo na open list
                (xi, yi) = self.mapa.desce(x,y)
                self.inserir_posicao_na_open_list( xi, yi, x, y, profundidade )            
    
                # Insere o vizinho da esquerda na open list
                (xe, ye) = self.mapa.esquerda(x,y)
                self.inserir_posicao_na_open_list( xe, ye, x, y, profundidade )  
                
                # Insere o vizinho da direita na open list
                (xd, yd) = self.mapa.direita(x,y)
                self.inserir_posicao_na_open_list( xd, yd, x, y, profundidade )  
            




    # Metodo que implementa o algoritmo de busca IDS
    def search( self, posicao_inicial, posicao_final ):

        numero_iteracoes = self.mapa.get_num_linhas() * self.mapa.get_num_colunas()
        retorno = False

        for i in range(numero_iteracoes):                                                   
            retorno = self.deapLimitedSearch( posicao_inicial, posicao_final, i )
            if( retorno ): 
                return retorno
            self.reset_variaveis_auxiliares()
        return retorno









