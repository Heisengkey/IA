#Algoritmo BFS

#Pedro Viegas

from platform import system
from estado import *
import os
from time import sleep

os.system("")

scramble = ''

def bfs(estadoInicial): #function for BFS

    visitado = []   # Estados ya visitados
    cola = [estadoInicial]       # Cola de estados que vamos a visitar   
    i = 0

    while cola and cola[0].depth <= 10:

        s = cola.pop(0)

        if s.getValor() not in visitado:

            visitado.append(s.getValor())

            cola += aplicaTransiciones(s)    # Aplica las transiciones posibles al estado actual y las añade a la cola
        i += 1
        if s.final:
            return s
    return visitado

def aplicaTransiciones(estado):
    # Aplica todas las transiciones definidas a nuestro estado
    # Comprueba que los estados generados por las transiciones son estados validos
    # Comentar las distinatas lineas para realizar pruebas de rendimiento segun los movimientos dados

    #Todos los movimientos elementales y rotaciones
    # return [estado.aplicaTransicion("F"), estado.aplicaTransicion("R"), estado.aplicaTransicion("U"), estado.aplicaTransicion("X"), estado.aplicaTransicion("Y"), estado.aplicaTransicion("Z")]

    #Todas las rotaciones y dos permutaciones Y y T (secuencias)
    # return [estado.aplicaTransicion("Yperm"), estado.aplicaTransicion("Tperm"), estado.aplicaTransicion("X"), estado.aplicaTransicion("Y"), estado.aplicaTransicion("Z")]
    
    #Todos los movimientos definidos
    # return [[estado.aplicaTransicion("F"), estado.aplicaTransicion("R"), estado.aplicaTransicion("U"), estado.aplicaTransicion("B"), estado.aplicaTransicion("L"), estado.aplicaTransicion("D"), estado.aplicaTransicion("X"), estado.aplicaTransicion("Y"), estado.aplicaTransicion("Z"), estado.aplicaTransicion("Yperm"), estado.aplicaTransicion("Tperm")]

    # Solo movimientos elementales
    return [estado.aplicaTransicion("F"), estado.aplicaTransicion("R"), estado.aplicaTransicion("U"), estado.aplicaTransicion("B"), estado.aplicaTransicion("L"), estado.aplicaTransicion("D")]


cubo = estado(["yvr", "yvn", "yan", "yar",
                "bvr", "bvn", "ban", "bar"])

cubo.pintaCubo()
scramble = input("Introduzca un Scramble: ")
cubo_scrambled = scramble_cube(cubo, scramble)
cubo_scrambled.pintaCubo()
input("Pulsa Enter para iniciar BFS.")
res = bfs(cubo_scrambled)
print(res)
res.pintaCubo()
