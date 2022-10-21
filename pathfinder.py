from collections import deque



class Pathfinder:


    def __init__( self ):
        self.matriz_auxiliar = []
        self.path_cost = 0
        self.path = deque()        


    # Metodo que cria uma matriz auxiliar para identificar se uma 
    # posicao do mapa ja foi ou nao visitada
    def criar_matriz_auxiliar( self, mapa ):

        numLinhas = mapa.get_num_linhas()
        numColunas = mapa.get_num_colunas()        
        
        for i in range(numLinhas):
            linha = numColunas * [0]
            self.matriz_auxiliar.append( linha )


    def visitar_posicao( self, x, y ):        
        self.matriz_auxiliar[y][x] = 1


    def posicao_ja_foi_visitada( self, x, y ):
        return self.matriz_auxiliar[y][x] == 1        






    def bfs( self, mapa, posicao_inicial, posicao_final ):

        self.criar_matriz_auxiliar( mapa )
        fronteira = deque()

        self.path_cost = 0
        self.path.append( posicao_inicial )
        if( posicao_inicial == posicao_final ):
            return

        

        #fronteira.append()
        #fronteira.popleft()

        pass

    
    def ids( self, mapa, posicao_inicial, posicao_final ):
        pass


    def ucs( self, mapa, posicao_inicial, posicao_final ):
        pass


    def greedy( self, mapa, posicao_inicial, posicao_final ):
        pass


    def a_star( self, mapa, posicao_inicial, posicao_final ):
        pass
    