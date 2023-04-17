import igraph as ip
import numpy as np

def criaMatriz(instancia):
    path = 'C:/Users/Felip/Documents/grafosmeu/Instancias/' + instancia + '.txt' # Define endereço de uma Instancia
    with open(path, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64") # Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data

def saidaResultado(instancia, matriz):
    print('\n' 'NOME DA INSTANCIA:', str(instancia)) # Imprime o nome da Instancia 
    linhas = matriz.shape[0] # Pega o primeiro elemento do array matriz que corresponde ao número de linhas
    colunas = matriz.shape[1] # Pega o segundo elemento do array matriz que corresponde ao número de colunas
    print("A matriz tem dimensões: " + str(linhas) + "x" + str(colunas) + '\n')
    path = 'C:/Users/Felip/Documents/grafosmeu/Resultados/' # Define o endereço de documento que armazenará os resultados
    arquivo = open(path + instancia +  '_dimensao', "a+") # Abre o arquivo no diretório definido pela  variável path
    arquivo.writelines(str(linhas) + ' ' + str(colunas) + '\n') # Escreve no documento resultados.txt o número de linhas e colunas da matriz lida
    arquivo.close # Fecha o arquivo

def criaListaAdjacencias(matriz):
    lista = {}
    for i in range(len(matriz)):
        lista[i] = []
        for j in range(len(matriz)):
            for x in range (matriz[i][j]):
                lista[i].append(j)
    print (lista)
    return lista

def insereArestaLista(listaAdj, vi, vj):
    if vi in listaAdj:
        idx = 0
        while idx < len(listaAdj[vi]) and listaAdj[vi][idx] < vj:
            idx += 1
        listaAdj[vi].insert(idx, vj)
    else:
        listaAdj[vi] = [vj]
    if vj in listaAdj:
        idx = 0
        while idx < len(listaAdj[vj]) and listaAdj[vj][idx] < vi:
            idx += 1
        listaAdj[vj].insert(idx, vi)
    else:
        listaAdj[vj] = [vi]


    print(listaAdj)
    return listaAdj

def removeArestaLista(listaAdj, vi, vj):
    # Verifica se vi e vj estão na lista de adjacências
    if vi in listaAdj and vj in listaAdj:
        # Remove a aresta da lista de adjacências
        if vj in listaAdj[vi]:
            listaAdj[vi].remove(vj)
        if vi in listaAdj[vj]:
            listaAdj[vj].remove(vi)
    print (listaAdj)
    return listaAdj

def removeVerticeLista(listaAdj, vi):
    # Percorre todas as listas de adjacências em busca de ocorrências de vi
    for v in listaAdj:
        # Remove todas as ocorrências de vi na lista de adjacências
        while vi in listaAdj[v]:
            listaAdj[v].remove(vi)
    # Remove a lista de adjacências de vi
    if vi in listaAdj:
        del listaAdj[vi]
    print(listaAdj)
    return listaAdj