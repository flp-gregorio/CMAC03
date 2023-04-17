import sys
import igraph as ip
import numpy as np

from getData import (entradaSaida as es, manipulaMatriz as mm, testes as ts) 

def main(instancia):
    matriz = es.criaMatriz(instancia)
    teste = es.insereArestaLista({0: [1, 1, 2, 2, 3], 1: [0, 0, 3], 2: [0, 0, 3], 3: [0, 1, 2]}, 0, 3)
    teste = es.insereArestaLista({0: [1, 2, 5], 1: [0], 2: [0, 3, 4, 5], 3: [2, 4, 6], 4: [2, 3], 5: [0, 2, 6], 6: [3, 5]}, 1, 5)

if __name__ == '__main__':
    main(str(sys.argv[1]))