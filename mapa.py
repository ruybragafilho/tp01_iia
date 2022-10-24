
class Mapa:
  
    # Tabela com o custo para percorrer cada tipo de terreno
    __custo_terreno = { '.': 1.0, 
                        ';': 1.5,
                        '+': 2.5,
                        'x': 6.0,
                        'X': 6.0 } 
  
    __parede = '@' 
  
  

    # inicializador da classe
    def __init__(self, matriz, w, h):
  
        self.__matriz = matriz
    
        self.__w_min = 0 # Limite aa esquerda do mapa
        self.__w_max = w-1 # Limite aa direita do mapa
    
        self.__h_min = 0 # Limite superior do mapa          
        self.__h_max = h-1 # Limite inferior do mapa   



    def get_num_linhas( self ): 
        return self.__h_max + 1

    def get_num_colunas( self ): 
        return self.__w_max + 1        


    # Metodo que determina de a posicao eh valida,
    # ou seja, se esta dentro dos limites do mapa 
    # e se a posicao nao eh uma parede. Se a posicao 
    # for valida, retorna True. Caso contrario, 
    # retorna False
    def posicao_eh_valida( self, x, y ):

        if( y >= self.__h_min  and y <= self.__h_max and
            x >= self.__w_min  and x <= self.__w_max and
            self.__matriz[y][x] != Mapa.__parede ):

            return True
        else:
            return False
  

  
    # Metodo que retorna o custo de passar pelo terreno
    # cuja posicao eh passada como parametro
    def custo( self, x, y ):
        return Mapa.__custo_terreno[ self.__matriz[y][x] ] 
  


    # Metodo que sobe uma posicao no mapa. Retorna uma tupla
    # representando com a nova posicao.
    def sobe(self, x, y):        
        return (x, y-1)
  
  
  
    # Metodo que desce uma posicao no mapa. Retorna uma tupla
    # representando com a nova posicao.
    def desce(self, x, y):
        return (x, y+1)    

  
  
    # Metodo que move uma posicao aa esquerda no mapa. Retorna uma tupla
    # representando com a nova posicao.
    def esquerda(self, x, y):
        return (x-1, y)    

  
  
    # Metodo que move uma posicao aa direita no mapa. Retorna uma tupla
    # representando com a nova posicao.
    def direita(self, x, y):
        return (x+1, y)
  
  
  
    # Metodo que mostra o mapa e suas dimensoes  
    def mostrar_mapa(self):
  
        print( 'w: ', self.__w_max + 1 )
        print( 'h: ', self.__h_max + 1 )
    
        for linha in range(self.__h_max + 1):
            print( '\n' )
            for coluna in range(self.__w_max + 1):
                print( self.__matriz[linha][coluna] )
            
  
# FIM DA DEFINICAO DA CLASSE MAPA














