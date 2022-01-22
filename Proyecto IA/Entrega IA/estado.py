colores = {
    "y" : '\33[103m',
    "b" : '\33[107m',
    "a" : '\33[104m',
    "v" : '\33[102m',
    "r" : '\33[101m',
    "n" : '\33[105m'
    }
CEND = '\033[0m'

caras = ['R', 'L', 'B', 'F', 'U', 'D']

from pickletools import read_uint1
from rubik import *

def getCara(cube, cara):
    if cara == 'R':
        return [cube[0][1], cube[1][1], cube[4][1], cube[5][1]]
    if cara == 'L':
        return [cube[2][1], cube[3][1], cube[6][1], cube[7][1]]
    if cara == 'U':
        return [cube[0][0], cube[1][0], cube[2][0], cube[3][0]]
    if cara == 'D':
        return [cube[4][0], cube[5][0], cube[6][0], cube[7][0]]
    if cara == 'F':
        return [cube[0][2], cube[3][2], cube[4][2], cube[7][2]]
    if cara == 'B':
        return [cube[1][2], cube[2][2], cube[5][2], cube[6][2]]

def esFinal(estado):
    res = True
    for cara in caras:
        carai = getCara(estado, cara)
        res = res and all(element == carai[0] for element in carai)
    return res

class estado:
    ##  Hace realmente falta que pongamos el ultimo elemento del movimiento? podemos añadirlo siempre la union del final al principio
    #   Asi ponemos hacer un map de los movimientos bien
    
    ##
    #   Cada valor en la lista representa una pieza, y la orientación actual que tiene
    #   [Up Right Front, Up Right Back, Up Left Back, Up Left Front,
    #   Down Right Front, Down Right Back, Down Left Back, Down Left Front]
    #   
    #   Dentro de cada pieza, identificamos con 3 letras los colores en cada posición 
    #       {b: Blanco, a: Azul, r: Rojo, n: Naranja, v: Verde, y: Amarillo}
    #   Siendo que la posición dentro de la cadena indica si este color se encuentra en el eje y(Up | Down), eje x(Right | Left), o eje z(Front | Back)
    #   Ya que sabemos que una pieza no puede tener a la vez dos caras en el mismo eje, por tanto con la cadena sacamos el color del eje que sea de la pieza
    #   y de su posición en la lista, sacarémos que caras en cada eje.
    #
    #   Por ejemplo:
    #       La primera pieza "bar", nos indica que en su eje y tendra Blanco, en su eje x Azul, y en su eje z Rojo.
    #       Como está en la primera posición de la lista, sabremos que es Up Right Front, por tanto tendrá el Blanco Arriba, Azul a la derecha, y Rojo en la frontal.
    #

    def actualizaFinal(self):
        self.final = esFinal(self.valor)

    def getValor(self):
        return self.valor
    
    def setValor(self, valor):
        self.valor = valor
        self.actualizaFinal()

    def getTransicion(self):
        return self.trans

    def pintaCubo(self):
        cube = self.valor

        print("\t"+colores[cube[6][2]] + " " + CEND, colores[cube[5][2]] + " " + CEND, "\n")
        print("\t"+colores[cube[2][2]] + " " + CEND, colores[cube[1][2]] + " " + CEND, "\n")
        print("   "+colores[cube[6][1]] + " " + CEND, colores[cube[2][1]] + " " + CEND, "\t"+colores[cube[2][0]] + " " + CEND, colores[cube[1][0]] + " " + CEND, colores[cube[1][1]] + " " + CEND, colores[cube[5][1]] + " " + CEND, colores[cube[5][0]] + " " + CEND, colores[cube[6][0]] + " " + CEND+ "\n")
        print("   "+colores[cube[7][1]] + " " + CEND, colores[cube[3][1]] + " " + CEND, "\t"+colores[cube[3][0]] + " " + CEND, colores[cube[0][0]] + " " + CEND, colores[cube[0][1]] + " " + CEND, colores[cube[4][1]] + " " + CEND, colores[cube[4][0]] + " " + CEND, colores[cube[7][0]] + " " + CEND+ "\n")
        print("\t"+colores[cube[3][2]] + " " + CEND, colores[cube[0][2]] + " " + CEND, "\n")
        print("\t"+colores[cube[7][2]] + " " + CEND, colores[cube[4][2]] + " " + CEND, "\n")

    def rota(self, movimiento):
        if movimiento == "R":
            return self.setValor(rotar_R(self.valor))
        if movimiento == "L":
            return self.setValor(rotar_Z(rotar_Z(rotar_R(rotar_Z(rotar_Z(self.valor))))))
        if movimiento == "U":
            return self.setValor(rotar_U(self.valor))
        if movimiento == "D":
            return self.setValor(rotar_Z(rotar_Z(rotar_U(rotar_Z(rotar_Z(self.valor))))))
        if movimiento == "F":
            return self.setValor(rotar_F(self.valor))
        if movimiento == "B":
            return self.setValor(rotar_X(rotar_X(rotar_F(rotar_X(rotar_X(self.valor))))))
        if movimiento == "X":
            return self.setValor(rotar_X(self.valor))
        if movimiento == "Y":
            return self.setValor(rotar_Y(self.valor))
        if movimiento == "Z":
            return self.setValor(rotar_Z(self.valor))
        if movimiento == "Tperm":
            return self.setValor(perm_T(self.valor))
        if movimiento == "Yperm":
            return self.setValor(perm_Y(self.valor))

    def aplicaTransicion(self, movimiento):
        # cara = list(map(lambda x: self.valor[x - 1], movimiento))    ## Sacamos las piezas que conforman la cara que estamos formando
        # cara.insert(0, cara.pop())                                  ## Rotamos las posiciones de las piezas en sentido horario
        # ## To-do
        # # hay que rotar las letras dentro de cada posición tambien.  
        # nuevo = list(map(lambda x: , self.valor))   ## Reincorporamos los valores desplazados a las posiciones que les corresponden y devolvemos un nuevo estado
        # ## Guardando el movimiento realizado y el valor nuevo actual

        # return estado([self.valor, movimiento])
        if movimiento == "R":
            return estado(rotar_R(self.valor), "R", self.depth + 1, self.path + "R")
        if movimiento == "L":
            return estado(rotar_Z(rotar_Z(rotar_R(rotar_Z(rotar_Z(self.valor))))), "L", self.depth + 1, self.path + "L")
        if movimiento == "U":
            return estado(rotar_U(self.valor), "U", self.depth + 1, self.path + "U")
        if movimiento == "D":
            return estado(rotar_Z(rotar_Z(rotar_U(rotar_Z(rotar_Z(self.valor))))), "D", self.depth + 1, self.path + "D")
        if movimiento == "F":
            return estado(rotar_F(self.valor), "F", self.depth + 1, self.path + "F")
        if movimiento == "B":
            return estado(rotar_X(rotar_X(rotar_F(rotar_X(rotar_X(self.valor))))), "B", self.depth + 1, self.path + "B")
        if movimiento == "X":
            return estado(rotar_X(self.valor), "X", self.depth + 1, self.path + "X")
        if movimiento == "Y":
            return estado(rotar_Y(self.valor), "Y", self.depth + 1, self.path + "Y")
        if movimiento == "Z":
            return estado(rotar_Z(self.valor), "Z", self.depth + 1, self.path + "Z")
        if movimiento == "Tperm":
            return estado(perm_T(self.valor), "T", self.depth + 1, self.path + "T")
        if movimiento == "Yperm":
            return estado(perm_Y(self.valor), "H", self.depth + 1, self.path + "H")
        

    def __init__(self, lsEstado, rotacion=0, depth=1, path='') -> None:
        self.valor = lsEstado
        self.trans = rotacion
        self.depth = depth
        self.path = path
        self.final = esFinal(lsEstado)
            
    def __str__(self) -> str:
        return f'{self.valor} ({procesaSecuencia(self.path)}) (Final?: {self.final})'
