#Algoritmo BFS

#Pedro Viegas

from estado import *

def bfs(estadoInicial, estadoFinal): #function for BFS

    visitado = []   # Estados ya visitados
    cola = [estadoInicial]       # Cola de estados que vamos a visitar   

    while cola:

        s = estado(cola.pop(0))

        if s not in visitado:

            visitado.append(s)

            cola += aplicaTransiciones(s)    # Aplica las transiciones posibles al estado actual y las añade a la cola

    return visitado

def aplicaTransiciones(estado):
    # Aplica todas las transiciones definidas a nuestro estado
    # Comprueba que los estados generados por las transiciones son estados validos
    return estado

print(bfs([[1, 2, 3, 4], 0], [[4, 3, 2, 1], 0]))