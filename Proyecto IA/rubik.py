# from estado import estado
import re


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

estadoS_R = ["rba", "bnv", "yra", "anb",
        "nay", "yvr", "yvn", "brv"]

movimiento = movimientos["R"]

def rotarAntihorario(pieza):
    return pieza[1:] + pieza[0]

def rotarHorario(pieza):
    return pieza[-1] + pieza[:-1]

def combinaciones(cadena):
    return [cadena, rotarAntihorario(cadena), rotarHorario(cadena)]

def rotar_R(estado):
    return estado

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
            # index = [i for i, item in enumerate(estadoIni) if re.search(r'^f"[{pieza}]+[{pieza}]+[{pieza}]"', item)]
            # print(index)
            # res.append(f'{index} -> {i} {"(90º)" if piezaFin == rotarHorario(estadoIni[index]) else "(-90º)"}')
            pass
    return res

print(diferenciaSecuencia(estadoS, estadoS_R))

prueba = "yra"
print(prueba)
print ("-------Antihorario (-90º)--------")
print(rotarAntihorario(prueba))
print ("-------Horario (90º)--------")
print(rotarHorario(prueba))