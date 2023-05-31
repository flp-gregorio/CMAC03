import igraph as ip
import numpy as np

def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] or  matriz[vj][vi] == 1:
         print(True)
    else:
        print(False)

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

def tipoGrafoLista(listaAdj):
    # Verifica se o grafo é um pseudografo
    if pseudografo(listaAdj):
        # Verifica se o grafo é dirigido
        if dirigido(listaAdj):
            print("31")
        else:
            print("30")
    # Verifica se o grafo é um multigrafo
    elif multigrafo(listaAdj):
        # Verifica se o grafo é dirigido
        if dirigido(listaAdj):
            print("21")
        else:
            print("20")
    # Verifica se o grafo é simples
    else:
        # Verifica se o grafo é dirigido
        if dirigido(listaAdj):
            print("1")
        else:
            print("0")

def dirigido(listaAdj):
    # Verifica se a lista de adjacências é simétrica
    for vi in listaAdj:
        for vj in listaAdj[vi]:
            if vi not in listaAdj[vj]:
                return True
    return False

def multigrafo(listaAdj):
    # Verifica se há pelo menos um vértice com múltiplas arestas
    for v in listaAdj:
        if len(listaAdj[v]) != len(set(listaAdj[v])):
            return True
    return False

def pseudografo(listaAdj):
    # Verifica se há algum laço
    for v in listaAdj:
        if v in listaAdj[v]:
            return True
    return False

def caminhoEuleriano(matriz):
    n,x = np.shape(matriz)
    total = 0 
    i = 0
    while((total <= 2) and (i <= n)):
        for v in range(n):
            if (np.sum(matriz[v]) % 2 != 0):
                total += 1
        i += 1
    if(total > 2):
        print(False)
        return False
    else:
        print(True)
        return True
    
def warshall(matriz):
    n,x = np.shape(matriz)
    matC = matriz

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(matC[i][j]) == 1 or (matC[i][k] == 1 and matC[k][j] == 1):
                    matC[i][j] = 1;
                else:
                    matC[i][j] = matC[i][j]
    matC = np.array(matC)
    print (matC)
    return 0

def DFS(lista, vertice):
    verificado = []
    adiciona_verificado(lista, vertice, verificado)
    print (verificado)
    return 0
    
def adiciona_verificado(lista, vertice, verificado):

    verificado.append(vertice)
    for adjacente in lista[vertice]:
        if adjacente not in verificado:
            adiciona_verificado(lista, adjacente, verificado)

def classificaArestas(adj_list, inicio=None):
    if inicio is None:
        inicio = 0

    classificacoes = []
    lista_tempo = {}
    tempo = [1]
    tempo[0] = 0
    cor = ['branco' for _ in range(len(adj_list))]
    tipoAresta = [[' ' for _ in range(len(adj_list))] for _ in range(len(adj_list))]
    tempoD = [0 for _ in range(len(adj_list))]
    tempoT = [0 for _ in range(len(adj_list))]

    def visitaDFS(vertice, parent):
        nonlocal tempo
        cor[vertice] = 'cinza'
        tempo[0] += 1
        tempoD[vertice] = tempo[0]

        for adj in adj_list[vertice]:
            if cor[adj] == 'branco':
                tipoAresta[vertice][adj] = 'Tree'
                classificacoes.append((vertice, adj, 'Tree'))
                visitaDFS(adj, vertice)
            elif cor[adj] == 'cinza':
                tipoAresta[vertice][adj] = 'Back'
                classificacoes.append((vertice, adj, 'Back'))
            else:
                if tempoD[vertice] < tempoD[adj]:
                    tipoAresta[vertice][adj] = 'Forward'
                    classificacoes.append((vertice, adj, 'Forward'))
                else:
                    tipoAresta[vertice][adj] = 'Cross'
                    classificacoes.append((vertice, adj, 'Cross'))
        
        cor[vertice] = 'preto'
        tempo[0] += 1
        tempoT[vertice] = tempo[0]

    for vertice in adj_list:
        if cor[vertice] == 'branco':
            visitaDFS(vertice, None)

    for vertice in adj_list:
        lista_tempo[vertice] = str(tempoD[vertice]) + '/' + str(tempoT[vertice])

    
    for aresta in classificacoes:
        print("{} {} {}".format(aresta[0], aresta[1], aresta[2]))

    return classificacoes

def ordenacaoTopologica(adj_list):
    # Função auxiliar para percorrer o grafo em profundidade e adicionar vértices à lista de saída
    def dfs(vertex, visited, stack):
        visited.add(vertex)
        
        for neighbor in adj_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor, visited, stack)
        
        stack.append(vertex)
    
    # Conjunto para acompanhar os vértices visitados
    visited = set()
    # Lista para armazenar a ordenação topológica dos vértices
    output = []
    
    # Percorre cada vértice do grafo
    for vertex in adj_list:
        if vertex not in visited:
            dfs(vertex, visited, output)
    
    # Inverte a ordem dos vértices na lista de saída para obter a ordenação topológica
    output.reverse()
    
    print (output)
    return output

def temposVertices(adjacencias, vertice_inicial):
    tempo = 0
    visitados = set()
    tempos = {}

    def dfs(vertice):
        nonlocal tempo
        visitados.add(vertice)
        tempo += 1
        tempos[vertice] = [tempo, None]  # Define apenas o tempo de descoberta (TD) inicialmente

        for adjacente in adjacencias.get(vertice, []):
            if adjacente not in visitados:
                dfs(adjacente)

        tempo += 1
        tempos[vertice][1] = tempo  # Define o tempo de término (TT) do vértice

    dfs(vertice_inicial)

    # Verifica se há vértices não visitados e os processa
    for vertice in adjacencias.keys():
        if vertice not in visitados:
            dfs(vertice)
            
            
    tempos_formatados = {v: f'{td}/{tt}' for v, (td, tt) in sorted(tempos.items())}
    print (tempos_formatados)

def verificaDAG(adj_list):
    visitados = {}
    ciclo = False

    def dfsDAG(v):
        nonlocal ciclo
        visitados[v] = 'cinza'

        for adjacente in adj_list[v]:
            if adjacente not in visitados:
                if dfsDAG(adjacente):
                    ciclo = True
            elif visitados[adjacente] == 'cinza':
                ciclo = True

        visitados[v] = 'preto'

    for v in adj_list:
        if v not in visitados:
            dfsDAG(v)
            if ciclo:
                print("NÃO DAG")
                return "NÃO DAG"

    print("DAG")
    return "DAG"