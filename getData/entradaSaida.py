import igraph as ip
import numpy as np

def criaMatriz(instancia):
    path = 'C:/Users/Felip/Documents/grafosmeu/Instancias/' + instancia + '.txt' # Define endereço de uma Instancia
    with open(path, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64") # Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data

def saidaResultado(instancia, matriz):
    print('\n' 'NOME DA INST NCIA:', str(instancia)) # Imprime o nome da Instancia 
    linhas = matriz.shape[0] # Pega o primeiro elemento do array matriz que corresponde ao número de linhas
    colunas = matriz.shape[1] # Pega o segundo elemento do array matriz que corresponde ao número de colunas
    print("A matriz tem dimensões: " + str(linhas) + "x" + str(colunas) + '\n')
    path = 'C:/Users/Felip/Documents/grafosmeu/resultados.txt' # Define o endereço de documento que armazenará os resultados
    arquivo = open(path, "a+") # Abre o arquivo no diretório definido pela  variável path
    arquivo.writelines(str(linhas) + ' ' + str(colunas) + '\n') # Escreve no documento resultados.txt o número de linhas e colunas da matriz lida
    arquivo.close # Fecha o arquivo
