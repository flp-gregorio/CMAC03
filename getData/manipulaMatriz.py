import igraph as ip
import numpy as np

def insereVertice(matriz):
    matriz = np.array(matriz)
    
    # Adiciona uma nova linha e coluna na matriz
    nova_linha = np.zeros(len(matriz))
    matriz = np.vstack([matriz, nova_linha])
    nova_coluna = np.zeros((len(matriz), 1))
    matriz = np.hstack([matriz, nova_coluna])
    matriz = np.array(matriz, 'int16')
    print(matriz)
    return matriz

def removeAresta(matriz, vi, vj):
    matriz[vi][vj] = 0
    matriz[vj][vi] = 0
    matriz = np.array(matriz)
    print(matriz) 
    return matriz

def removeVertice(matriz, v):
    matriz = np.array(matriz, 'int16')
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][v] = -1
            matriz[v][j] = -1

    print(matriz) 
    return matriz

def  insereAresta(matrix, vi, vj):
    if matrix[vi][vj] == matrix[vj][vi]:
        matrix[vi][vj] = matrix[vi][vj] + 1
        matrix[vj][vi] = matrix[vj][vi] + 1
    else:
        matrix[vi][vj] = matrix[vi][vj] + 1
    print(matrix)
    
def  insereAresta(matrix, vi, vj):
    if matrix[vi][vj] == matrix[vj][vi]:
        matrix[vi][vj] = matrix[vi][vj] + 1
        matrix[vj][vi] = matrix[vj][vi] + 1
    else:
        matrix[vi][vj] = matrix[vi][vj] + 1
    print(matrix)
    return matrix