import numpy as np

def calcDensidade(matriz):
    n = len(matriz)
    m = sum([sum(linha) for linha in matriz])
    print(round(m / (n * (n - 1)), 3))

def calcDensidadeLista(listaAdj):
    # Calcula o número de vértices e arestas do grafo
    num_vertices = len(listaAdj)
    num_arestas = sum([len(vizinhos) for vizinhos in listaAdj.values()])
    
    # Calcula o número máximo de arestas que o grafo pode ter, 
    # considerando se é um multigrafo e/ou grafo dirigido
    if multigrafo(listaAdj):
        max_arestas = num_vertices * (num_vertices - 1)
    else:
        max_arestas = num_vertices * (num_vertices - 1) // 2
    if dirigido(listaAdj):
        max_arestas *= 2
    
    # Calcula a densidade do grafo e arredonda para 3 casas decimais
    densidade = round(num_arestas / max_arestas, 3)
    
    print(densidade)
    return densidade
        
def dirigido(listaAdj):
    # Verifica se o grafo é dirigido, verificando se cada aresta 
    # tem a sua inversa na lista de adjacências
    for i in listaAdj:
        for j in listaAdj[i]:
            if i not in listaAdj[j]:
                return True
    return False

def multigrafo(listaAdj):
    # Verifica se o grafo é um multigrafo, verificando se existem 
    # duas arestas com o mesmo par de vértices
    arestas = set()
    for vertice, vizinhos in listaAdj.items():
        for vizinho in vizinhos:
            if (vertice, vizinho) in arestas or (vizinho, vertice) in arestas:
                return True
            else:
                arestas.add((vertice, vizinho))
    return False