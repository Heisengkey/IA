#Algoritmo BFS

#Pedro Viegas

from platform import system
from estado import *
import os
import time

os.system("")

def bfs(estadoInicial, estadoFinal): #function for BFS

    visitado = []   # Estados ya visitados
    cola = [estadoInicial]       # Cola de estados que vamos a visitar   

    while cola:

        s = cola.pop(0)

        if s not in visitado:

            visitado.append(s)

            cola += aplicaTransiciones(s)    # Aplica las transiciones posibles al estado actual y las añade a la cola

    return visitado

def aplicaTransiciones(estado):
    # Aplica todas las transiciones definidas a nuestro estado
    # Comprueba que los estados generados por las transiciones son estados validos
    return [estado.aplicaTransicion("R"), estado.aplicaTransicion("F"), estado.aplicaTransicion("U"), estado.aplicaTransicion("X"), estado.aplicaTransicion("Y"), estado.aplicaTransicion("Z")]

cubo = estado(["yvr", "yvn", "yan", "yar",
                "bvr", "bvn", "ban", "bar"])

cubo_solved = estado(["yvr", "yvn", "yan", "yar",
                "bvr", "bvn", "ban", "bar"])

# res = bfs(cubo, cubo_solved)

# cuboR = estado(estadoS_R)
# print(cubo)
# print(cubo.esFinal())
os.system("cls")
os.system("clear")
cubo.pintaCubo()
for i in range(4):
    time.sleep(0.5)
    os.system("cls")
    os.system("clear")
    cubo = cubo.aplicaTransicion("B")
    cubo.pintaCubo()


# print("\tB", "B", "", "", "", "\n")
# print("\tB", "B", "", "", "", "\n")
# print("   L", "L", "\tU", "U", "R", "R", "D", "D\n")
# print("   L", "L", "\tU", "U", "R", "R", "D", "D\n")
# print("\tF", "F", "", "", "", "\n")
# print("\tF", "F", "", "", "", "\n")