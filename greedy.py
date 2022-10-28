# Módulo que implementa o algoritmo de busca gulosa - Greegy
# Autor: Ruy Braga Filho


from collections import deque
from mapa import Mapa


class Greedy:

    status_posicao = { 'posicao_virgem': 0,
                       'open_list': 1,
                       'explorado': 2  }


    def __init__( self, mapa ):

        self.mapa = mapa
        self.matriz_status_visita = []
        self.matriz_de_antecessores = []

        self.path = deque()        
        self.path_cost = 0

        self.open_list = deque()


    # Metodo que cria uma matriz auxiliar para identificar se uma 
    # posicao do mapa ja foi ou nao visitada
    def criar_matriz_status_visita( self ):

        numLinhas = self.mapa.get_num_linhas()
        numColunas = self.mapa.get_num_colunas()        
        
        for i in range(numLinhas):
            linha = numColunas * [  Greedy.status_posicao['posicao_virgem']  ]
            self.matriz_status_visita.append( linha )


    # Metodo que cria uma matriz auxiliar para armazenar a 
    # posicao antecessora de cada posicao visitada no mapa 
    def criar_matriz_de_antecessores( self ):

        numLinhas = self.mapa.get_num_linhas()
        numColunas = self.mapa.get_num_colunas()        
        
        for i in range(numLinhas):
            linha = numColunas * [ (-1,-1) ]
            self.matriz_de_antecessores.append( linha )     


    # Metodo que retorna True se a posicao nunca entrou na open_list 
    # e nunca foi explorada
    def posicao_nao_foi_visitada( self, x, y ):
        return self.matriz_status_visita[y][x] == Greedy.status_posicao['posicao_virgem']                    


    # Metodo que insere a posicao (x,y) na open list e registra
    # as coordenadas do seu antecessor na matriz de antecessor 
    def inserir_posicao_na_open_list( self, x, y, x_antecessor, y_antecessor ):  

        if( self.mapa.posicao_eh_valida( x, y ) and 
            self.posicao_nao_foi_visitada( x, y ) ):     

            self.matriz_status_visita[y][x] = Greedy.status_posicao['open_list']
            self.open_list.append( (x,y) )

            self.matriz_de_antecessores[y][x] = (y_antecessor, x_antecessor)


    # Metodo que retorna o custo do caminho encontrado pelo bfs
    def get_path_cost( self ):
        return self.path_cost


    # Metodo que utiliza a matriz de antecessores para retornar
    # o caminho encontrado pelo bfs
    def get_path( self, posicao_inicial, posicao_final ):

        (x, y) = posicao_final
        self.path.appendleft( (x,y) )
        self.path_cost += self.mapa.custo(x, y)

        while( True ):
            (y, x) = self.matriz_de_antecessores[y][x]
            self.path.appendleft( (x,y) )
            if( (x,y) == posicao_inicial ):
                break
            self.path_cost += self.mapa.custo(x, y)        

        return self.path


    # Metodo que implementa o algoritmo de busca BFS
    def pathfinder( self, posicao_inicial, posicao_final ):
        
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
            self.matriz_status_visita[y][x] = Greedy.status_posicao['explorado']

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
            


            
