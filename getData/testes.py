import igraph as ip
import numpy as np

def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] or  matriz[vj][vi] == 1:
         print(True)
    else:
        print(False)

def calcDensidade(matriz):
    n = len(matriz)
    m = sum([sum(linha) for linha in matriz])
    print(round(m / (n * (n - 1)), 3))

'''def tipoGrafo(matriz):
    n = len(matriz)
    simetrica = all(matriz[i][j] == matriz[j][i] for i in range(n) for j in range(n))
    diagonal_nula = all(matriz[i][i] == 0 for i in range(n))
    if simetrica:
        if diagonal_nula:
            for i in range(n):
                for j in range(i+1, n):
                    if matriz[i][j] > 1:
                        print(20)
                        return "Multigrafo"
            print (0)
            return "Grafo simples"
        else:
            for i in range(n):
                for j in range(n):
                    if matriz[i][j] > 1:
                        print(21)
                        return "Multigrafo dirigido"
                if matriz[i][i] > 0:
                    print(31)
                    return "Pseudografo dirigido"
            print(1)
            return "Digrafo"
    else:
        if diagonal_nula:
            for i in range(n):
                for j in range(i+1, n):
                    if matriz[i][j] > 1:
                        print(21)
                        return "Multigrafo dirigido"
            for i in range(n):
                for j in range(i+1, n):
                    if matriz[i][j] != 0 and matriz[j][i] != 0:
                        print(31)
                        return "Pseudografo dirigido"
            print(1)
            return "Digrafo"
        else:
            for i in range(n):
                for j in range(i+1, n):
                    if matriz[i][j] > 1 or matriz[j][i] > 1:
                        print(20)
                        return "Multigrafo"
            print(30)
            return "Pseudografo"'''

def tipoGrafo(matriz):
    if pseudografo(matriz):
        if dirigido(matriz):
            print(31)
        else:
            print(30)
    elif multigrafo(matriz):
        if dirigido(matriz):
            print(21)
        else:
            print(20)
    else:
        if dirigido(matriz):
            print(1)
        else:
            print(0)

def dirigido(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return 1
    return 0

def multigrafo(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > 1 or matriz[j][i] > 1:
                return 1
    return 0

def pseudografo(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] != 0 and multigrafo(matriz):
            return 1
    return 0

def verificaAdjacenciaLista(listaAdj, vi, vj):
    # Verifica se vi e vj estão na lista de adjacências
    if vi not in listaAdj or vj not in listaAdj:
        print("False1")
        return False
    # Verifica se vj está na lista de adjacências de vi
    if vj in listaAdj[vi]:
        print("True1")
        return True
    # Verifica se vi está na lista de adjacências de vj (caso seja um grafo não-direcionado)
    if vj in listaAdj and vi in listaAdj[vj]:
        print("True2")
        return True
    # Se não houver adjacência entre os vértices, retorna False
    print("False5")
    return False
