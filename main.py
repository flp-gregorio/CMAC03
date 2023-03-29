import sys

from getData import (entradaSaida as es) 

def main(instancia):
    matriz = es.criaMatriz(instancia)
    es.saidaResultado(instancia, matriz)

if __name__ == '__main__':
    main(str(sys.argv[1]))