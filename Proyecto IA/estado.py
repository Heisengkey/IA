movimientos = {
        "R" : [1, 2, 6, 5],
        "L" : [4, 8, 7, 3],
        "U" : [2, 3, 7, 6],
        "D" : [1, 5, 8, 4],
        "F" : [1, 4, 3, 2],
        "B" : [8, 5, 6, 7]        
        }
colores = {
    "y" : '\33[103m',
    "b" : '\33[107m',
    "a" : '\33[104m',
    "v" : '\33[102m',
    "r" : '\33[101m',
    "n" : '\33[105m'
    }
CEND = '\033[0m'

from rubik import *

class estado:
    final = ["bar", "ban", "bvn", "bvr",
            "yar", "yan", "yvn", "yvr"]

    final2 = ["yvr", "yvn", "yan", "yar",
                "bvr", "bvn", "ban", "bar"]

    # movimientos = {
    #     "R" : [1, 2, 6, 5, 1],
    #     "L" : [4, 8, 7, 3, 4],
    #     "U" : [2, 3, 7, 6, 2],
    #     "D" : [1, 5, 8, 4, 1],
    #     "F" : [1, 4, 3, 2, 1],
    #     "B" : [8, 5, 6, 7, 8]        
    # }
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

    def __init__(self, lsEstado, rotacion=0) -> None:
        self.valor = lsEstado
        self.trans = rotacion
    
    def __str__(self) -> str:
        return str(self.valor) + " realizando " + str(self.trans)

    def getValor(self):
        return self.valor

    def getTransicion(self):
        return self.trans

    def esFinal(self):
        cube = self.valor

        return (cube[0][0] == cube[1][0] and cube[1][0] == cube[2][0] and cube[2][0] == cube[3][0] and   #son iguales todas las de la cara UP
                cube[4][0] == cube[5][0] and cube[5][0] == cube[6][0] and cube[6][0] == cube[7][0] and  #son iguales todas las de la cara DOWN
                cube[0][1] == cube[1][1] and cube[1][1] == cube[4][1] and cube[4][1] == cube[5][1] and  #son iguales todas las de la cara RIGHT
                cube[2][1] == cube[3][1] and cube[3][1] == cube[6][1] and cube[6][1] == cube[7][1] and  #son iguales todas las de la cara LEFT
                cube[0][2] == cube[3][2] and cube[3][2] == cube[4][2] and cube[4][2] == cube[7][2] and  #son iguales todas las de la cara FRONT
                cube[1][2] == cube[2][2] and cube[2][2] == cube[5][2] and cube[5][2] == cube[6][2])     #son iguales todas las de la cara BACK

    def pintaCubo(self):
        cube = self.valor

        print("\t"+colores[cube[6][2]] + " " + CEND, colores[cube[5][2]] + " " + CEND, "\n")
        print("\t"+colores[cube[2][2]] + " " + CEND, colores[cube[1][2]] + " " + CEND, "\n")
        print("   "+colores[cube[6][1]] + " " + CEND, colores[cube[2][1]] + " " + CEND, "\t"+colores[cube[2][0]] + " " + CEND, colores[cube[1][0]] + " " + CEND, colores[cube[1][1]] + " " + CEND, colores[cube[5][1]] + " " + CEND, colores[cube[5][0]] + " " + CEND, colores[cube[6][0]] + " " + CEND+ "\n")
        print("   "+colores[cube[7][1]] + " " + CEND, colores[cube[3][1]] + " " + CEND, "\t"+colores[cube[3][0]] + " " + CEND, colores[cube[0][0]] + " " + CEND, colores[cube[0][1]] + " " + CEND, colores[cube[4][1]] + " " + CEND, colores[cube[4][0]] + " " + CEND, colores[cube[7][0]] + " " + CEND+ "\n")
        print("\t"+colores[cube[3][2]] + " " + CEND, colores[cube[0][2]] + " " + CEND, "\n")
        print("\t"+colores[cube[7][2]] + " " + CEND, colores[cube[4][2]] + " " + CEND, "\n")

    def aplicaTransicion(self, movimiento):
        # cara = list(map(lambda x: self.valor[x - 1], movimiento))    ## Sacamos las piezas que conforman la cara que estamos formando
        # cara.insert(0, cara.pop())                                  ## Rotamos las posiciones de las piezas en sentido horario
        # ## To-do
        # # hay que rotar las letras dentro de cada posición tambien.  
        # nuevo = list(map(lambda x: , self.valor))   ## Reincorporamos los valores desplazados a las posiciones que les corresponden y devolvemos un nuevo estado
        # ## Guardando el movimiento realizado y el valor nuevo actual

        # return estado([self.valor, movimiento])
        if movimiento == "R":
            return estado(rotar_R(self.valor), "R")
        if movimiento == "L":
            return estado(rotar_Z(rotar_Z(rotar_R(rotar_Z(rotar_Z(self.valor))))), "L")
        if movimiento == "U":
            return estado(rotar_U(self.valor), "U")
        if movimiento == "D":
            return estado(rotar_Z(rotar_Z(rotar_U(rotar_Z(rotar_Z(self.valor))))), "D")
        if movimiento == "F":
            return estado(rotar_F(self.valor), "F")
        if movimiento == "B":
            return estado(rotar_X(rotar_X(rotar_F(rotar_X(rotar_X(self.valor))))), "B")
        if movimiento == "X":
            return estado(rotar_X(self.valor), "X")
        if movimiento == "Y":
            return estado(rotar_Y(self.valor), "Y")
        if movimiento == "Z":
            return estado(rotar_Z(self.valor), "Z")

