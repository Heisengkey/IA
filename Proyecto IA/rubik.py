# from estado import estado
import re
import itertools

movimientos = {
    "R": [1, 2, 6, 5],
    "L": [4, 8, 7, 3],
    "U": [2, 3, 7, 6],
    "D": [1, 5, 8, 4],
    "F": [1, 4, 3, 2],
    "B": [8, 5, 6, 7],
}

final = ["bar", "ban", "bvn", "bvr",
        "yar", "yan", "yvn", "yvr"]


est = ["bar", "ban", "bvn", "bvr",
        "yar", "yan", "yvn", "yvr"]

estadoS = ["vnb", "rvy", "yra", "anb",
        "abr", "yan", "yvn", "brv"]

solved_Yellow_Up = ["yvr", "yvn", "yan", "yar",
                "bvr", "bvn", "ban", "bar"]

estadoS_R = ["rvb", "rvy", "yan", "yar",
            "nvb", "nvy", "ban", "bar"]

estadoS_L = ["yvr", "yvn", "nab", "nay",
                "bvr", "bvn", "rab", "ray"]

estadoS_U = ["ynv", "yna", "yra", "yrv",
                "bvr", "bvn", "ban", "bar"]

estadoS_D = ["yvr", "yvn", "yan", "yar",
                "bra", "brv", "bnv", "bna"]

estadoS_F = ["ayr", "yvn", "yan", "abr",
                "vyr", "bvn", "ban", "vbr"]

estadoS_B = ["yvr", "vbn", "vyn", "yar",
                "bvr", "abn", "ayn", "bar"]

estadoS_X = ["rvb", "rvy", "ray", "rab",
                "nvb", "nvy", "nay", "nab"]

estadoS_Y = ["ynv", "yna", "yra", "yrv",
                "bnv", "bna", "bra", "brv"]

estadoS_Z = ["ayr", "ayn", "abn", "abr",
                "vyr", "vyn", "vbn", "vbr"]


movimiento = movimientos["R"]

def rotarPegatinaR(pieza):
    return pieza[-1] + pieza[1] + pieza[0]

def rotarPegatinaU(pieza):
    return pieza[0] + pieza[-1] + pieza[1]

def rotarPegatinaF(pieza):
    return pieza[1] + pieza[0] + pieza[-1]

def combinacionesR(cadena):
    return [cadena, rotarPegatinaR(cadena), rotarPegatinaR(rotarPegatinaR(cadena))]

def rotar_R(estado):
    return [rotarPegatinaR(estado[4]), rotarPegatinaR(estado[0]), estado[2], estado[3], rotarPegatinaR(estado[5]), rotarPegatinaR(estado[1]), estado[6], estado[7]]

def rotar_U(estado):
    return [rotarPegatinaU(estado[1]), rotarPegatinaU(estado[2]), rotarPegatinaU(estado[3]), rotarPegatinaU(estado[0]), estado[4], estado[5], estado[6], estado[7]]

def rotar_F(estado):
    return [rotarPegatinaF(estado[3]), estado[1], estado[2], rotarPegatinaF(estado[7]), rotarPegatinaF(estado[0]), estado[5], estado[6], rotarPegatinaF(estado[4])]

def rotar_Rp(estado):
    return rotar_R(rotar_R(rotar_R(estado)))

def rotar_Up(estado):
    return rotar_U(rotar_U(rotar_U(estado)))

def rotar_Fp(estado):
    return rotar_F(rotar_F(rotar_F(estado)))

def rotar_X(estado):
    return [rotarPegatinaR(estado[4]), rotarPegatinaR(estado[0]), rotarPegatinaR(estado[3]), rotarPegatinaR(estado[7]), rotarPegatinaR(estado[5]), rotarPegatinaR(estado[1]), rotarPegatinaR(estado[2]), rotarPegatinaR(estado[6])]

def rotar_Y(estado):
    return [rotarPegatinaU(estado[1]), rotarPegatinaU(estado[2]), rotarPegatinaU(estado[3]), rotarPegatinaU(estado[0]), rotarPegatinaU(estado[5]), rotarPegatinaU(estado[6]), rotarPegatinaU(estado[7]), rotarPegatinaU(estado[4])]

def rotar_Z(estado):
    return [rotarPegatinaF(estado[3]), rotarPegatinaF(estado[2]), rotarPegatinaF(estado[6]), rotarPegatinaF(estado[7]), rotarPegatinaF(estado[0]), rotarPegatinaF(estado[1]), rotarPegatinaF(estado[5]), rotarPegatinaF(estado[4])]

def diferenciaSecuencia(estadoIni, estadoFin):
    res = []
    for i in range(len(estadoIni)):
        piezaIni = estadoIni[i]
        piezaFin = estadoFin[i]
        if piezaIni == piezaFin:
            res.append("=")
        else:
            # Si no está la pieza en su misma posición y rotación, miramos en que posición está usando la expresión regular.
            # De esta forma podemos introducir dos estados, y nos dirá las diferencias finales entre estos dos, para facilitar la programación manual
            # de las transiciones en el BFS.
            # 

            if rotarPegatinaR(piezaFin) in estadoIni: #deshacemos el posible movimiento de rotacion de la pieza, para saber si esta contenida en el estado inicial
                res.append(f'{estadoIni.index(rotarPegatinaR(piezaFin))} -> {i} R') #como supusimos que se realizó una rotacion antihoraria, y la deshicimos...
            elif rotarPegatinaU(piezaFin) in estadoIni: #deshacemos el posible movimiento de rotacion de la pieza, para saber si esta contenida en el estado inicial
                res.append(f'{estadoIni.index(rotarPegatinaU(piezaFin))} -> {i} U')
            elif rotarPegatinaF(piezaFin) in estadoIni: #deshacemos el posible movimiento de rotacion de la pieza, para saber si esta contenida en el estado inicial
                res.append(f'{estadoIni.index(rotarPegatinaF(piezaFin))} -> {i} F')
            else:
                res.append(f'{estadoIni.index(piezaFin)} -> {i}')
    return res

# # print (solved_Yellow_Up[0])
# # print (rotarPegatinaR(solved_Yellow_Up[0]))
# # print (rotarPegatinaR(rotarPegatinaR(solved_Yellow_Up[0])))
# print("Movimiento R", diferenciaSecuencia(solved_Yellow_Up, estadoS_R), "\n")
# print("Movimiento L", diferenciaSecuencia(solved_Yellow_Up, estadoS_L), "\n")
# print("Movimiento U", diferenciaSecuencia(solved_Yellow_Up, estadoS_U), "\n")
# print("Movimiento D", diferenciaSecuencia(solved_Yellow_Up, estadoS_D), "\n")
# print("Movimiento F", diferenciaSecuencia(solved_Yellow_Up, estadoS_F), "\n")
# print("Movimiento B", diferenciaSecuencia(solved_Yellow_Up, estadoS_B), "\n")
# print("Rotacion X", diferenciaSecuencia(solved_Yellow_Up, estadoS_X), "\n")
# print("Rotacion Y", diferenciaSecuencia(solved_Yellow_Up, estadoS_Y), "\n")
# print("Rotacion Z", diferenciaSecuencia(solved_Yellow_Up, estadoS_Z), "\n")
# # # print(list(itertools.permutations(["y", "v", "r"])))
# # # [('y', 'v', 'r'), ('v', 'r', 'y'), ('r', 'y', 'v')]
# # print(solved_Yellow_Up)
# # print(estadoS_R)
# # print(estadoS_R[0] in solved_Yellow_Up)
# # print('yvr' in solved_Yellow_Up)
# # print(rotarHorario(solved_Yellow_Up[0]) == rotarAntihorario(solved_Yellow_Up[0]))
# # print(rotarHorario(solved_Yellow_Up[0]) == 'ryv')
# # # prueba = "yra"
# # # print(prueba)
# # # print ("-------Antihorario (-90º)--------")
# # # print(rotarAntihorario(prueba))
# # # print ("-------Horario (90º)--------")
# # # print(rotarHorario(prueba))