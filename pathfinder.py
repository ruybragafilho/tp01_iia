# Módulo que implementa a super classe Pathfinder, que será 
# pai das classes que implementam os metodos de busca
# Autor: Ruy Braga Filho


from collections import deque
from mapa import Mapa


class Pathfinder:

    status_posicao = { 'posicao_virgem': 0,
                       'open_list': 1,
                       'expandida': 2  }

    antecessor_vazio = (-1, -1)


    def __init__( self, mapa ):

        self.mapa = mapa
        self.matriz_status_visita = []
        self.matriz_de_antecessores = []

        self.path = deque()        
        self.path_cost = 0

        self.open_list = deque()



    # Metodo que cria uma matriz com as mesmas dimensoes do atributo mapa
    # e a inicializa com o valor passado como parametro
    def criar_matriz( self, matriz, valor ):

        numLinhas = self.mapa.get_num_linhas()
        numColunas = self.mapa.get_num_colunas()        
        
        for i in range(numLinhas):
            linha = numColunas * [  valor  ]
            matriz.append( linha )    



    # Metodo que cria uma matriz auxiliar para identificar se uma 
    # posicao do mapa ja foi ou nao visitada
    def criar_matriz_status_visita( self ):

        matriz = self.matriz_status_visita
        valor = Pathfinder.status_posicao['posicao_virgem']
        self.criar_matriz( matriz, valor )



    # Metodo que cria uma matriz auxiliar para armazenar a 
    # posicao antecessora de cada posicao visitada no mapa 
    def criar_matriz_de_antecessores( self ):

        matriz = self.matriz_de_antecessores
        valor = Pathfinder.antecessor_vazio
        self.criar_matriz( matriz, valor )        



    # Metodo que retorna True se a posicao nunca entrou na open_list 
    # e nunca foi explorada
    def posicao_nao_foi_visitada( self, x, y ):
        return self.matriz_status_visita[y][x] == Pathfinder.status_posicao['posicao_virgem']                    

    # Metodo que retorna True se a posicao estah na open_list 
    def posicao_na_open_list( self, x, y ):
        return self.matriz_status_visita[y][x] == Pathfinder.status_posicao['open_list']                            

    # Metodo que retorna True se a posicao foi expandida
    def posicao_expandida( self, x, y ):
        return self.matriz_status_visita[y][x] == Pathfinder.status_posicao['expandida']                                    


    # Metodo que insere a posicao (x,y) na open list e registra
    # as coordenadas do seu antecessor na matriz de antecessor 
    def inserir_posicao_na_open_list( self, x, y, x_antecessor, y_antecessor ):  

        if( self.mapa.posicao_eh_valida( x, y ) and 
            self.posicao_nao_foi_visitada( x, y ) ):     

            self.matriz_status_visita[y][x] = Pathfinder.status_posicao['open_list']
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


            


            
