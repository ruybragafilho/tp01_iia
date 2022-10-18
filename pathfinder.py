#! /usr/bin/env python3

import sys






def main():

    arquivo_entrada = sys.argv[1]
    identificador_metodo = sys.argv[2]

    xi = sys.argv[3]
    yi = sys.argv[4]

    xf = sys.argv[5]
    yf = sys.argv[6]

    print( '\n\n' )

    print( 'arquivo_entrada: ', arquivo_entrada )
    print( 'identificador_metodo: ', identificador_metodo )
    print( 'xi: ', xi )
    print( 'yi: ', yi )
    print( 'xf: ', xf )
    print( 'yf: ', yf )

    print( '\nNumero grande: ', 2.0**32 )

    print( '\n\n' )

    

main()