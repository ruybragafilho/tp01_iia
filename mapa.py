
class Mapa:
  
    # Tabela com o custo para percorrer cada tipo de terreno
    custo_terreno = { '.': 1.0, 
                      ';': 1.5,
                      '+': 2.5,
                      'x': 6.0,
                      'X': 6.0 } 
  
    parede = '@' 
  
  
    # inicializador da classe
    def __init__(self, matriz, w, h):
  
        self.matriz = matriz
    
        self.w_min = 0 # Limite aa esquerda do mapa
        self.w_max = w-1 # Limite aa direita do mapa
    
        self.h_min = 0 # Limite superior do mapa          
        self.h_max = h-1 # Limite inferior do mapa   

        print( self.w_max )
        print( self.h_max )
  
      
  
  
  
    # Metodo que tenta subir uma posicao no mapa.
    # Se a posicao acima for invalida, retorna booleano False.
    # Se a posicao acima for valida, retorna uma lista contendo uma tupla com 
    # as coordenadas (x,y) da posicao acima e um float com o custo para percorrer 
    # o terreno da posicao acima: [ (x,y), custo ].
    def sobe(self, x_atual, y_atual):
  
        y_acima = y_atual-1 
    
        if( y_acima < self.h_min  or  self.matriz[y_acima][x_atual] == Mapa.parede ):
            return False    
        else:
            return [ (x_atual, y_acima), Mapa.custo_terreno[ self.matriz[y_acima][x_atual] ]]
  
  
  
    # Metodo que tenta descer uma posicao no mapa
    # Se a posicao abaixo for invalida, retorna booleano False.
    # Se a posicao abaixo for valida, retorna uma lista contendo uma tupla com 
    # as coordenadas (x,y) da posicao abaixo e um float com o custo para percorrer 
    # o terreno da posicao abaixo: [ (x,y), custo ].
    def desce(self, x_atual, y_atual):
  
        y_abaixo = y_atual+1 
    
        if( y_abaixo > self.h_max  or  self.matriz[y_abaixo][x_atual] == Mapa.parede ):
            return False    
        else:
            return [ (x_atual, y_abaixo), Mapa.custo_terreno[ self.matriz[y_abaixo][x_atual] ]]
  
  
  
    # Metodo que tenta mover uma posicao aa esquerda no mapa
    # Se a posicao aa esquerda for invalida, retorna booleano False.
    # Se a posicao aa esquerda for valida, retorna uma lista contendo uma tupla com 
    # as coordenadas (x,y) da posicao aa esquerda e um float com o custo para percorrer 
    # o terreno da posicao aa esquerda: [ (x,y), custo ].
    def esquerda(self, x_atual, y_atual):
  
        x_esquerda = x_atual-1 
        
        if( x_esquerda < self.w_min  or  self.matriz[y_atual][x_esquerda] == Mapa.parede ):
            return False    
        else:
            return [ (x_esquerda, y_atual), Mapa.custo_terreno[ self.matriz[y_atual][x_esquerda] ]]
  
  
  
    # Metodo que tenta mover uma posicao aa direita no mapa
    # Se a posicao aa direita for invalida, retorna booleano False.
    # Se a posicao aa direita for valida, retorna uma lista contendo uma tupla com 
    # as coordenadas (x,y) da posicao aa direita e um float com o custo para percorrer 
    # o terreno da posicao aa direita: [ (x,y), custo ].
    def direita(self, x_atual, y_atual):
  
        x_direita = x_atual+1 
        
        if( x_direita > self.w_max  or  self.matriz[y_atual][x_direita] == Mapa.parede ):
            return False    
        else:
            return [ (x_direita, y_atual), Mapa.custo_terreno[ self.matriz[y_atual][x_direita] ]]
  
  
  
    # Metodo que mostra o mapa e suas dimensoes  
    def mostrar_mapa(self):
  
        print( 'w: ', self.w_max + 1 )
        print( 'h: ', self.h_max + 1 )
    
        for linha in range(self.h_max + 1):
            print( '\n' )
            for coluna in range(self.w_max + 1):
                print( self.matriz[linha][coluna] )
            
  
# FIM DA DEFINICAO DA CLASSE MAPA














