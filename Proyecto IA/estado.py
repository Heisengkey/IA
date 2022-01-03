class estado:
    final = ["bar", "ban", "bvn", "bvr",
             "yar", "yan", "yvn", "yvr"]

    # movimientos = {
    #     "R" : [1, 2, 6, 5, 1],
    #     "L" : [4, 8, 7, 3, 4],
    #     "U" : [2, 3, 7, 6, 2],
    #     "D" : [1, 5, 8, 4, 1],
    #     "F" : [1, 4, 3, 2, 1],
    #     "B" : [8, 5, 6, 7, 8]        
    # }
    movimientos = {
        "R" : [1, 2, 6, 5],
        "L" : [4, 8, 7, 3],
        "U" : [2, 3, 7, 6],
        "D" : [1, 5, 8, 4],
        "F" : [1, 4, 3, 2],
        "B" : [8, 5, 6, 7]        
    }
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

    def __init__(self, lsEstado) -> None:
        self.valor = lsEstado[0]
        self.trans = lsEstado[1]
    
    def __str__(self) -> str:
        return str(self.valor) + " realizando " + str(self.trans)

    def getValor(self):
        return self.valor

    def getTransicion(self):
        return self.trans

    def esFinal(self):
        return self.valor == self.final

    def aplicaTransicion(self, movimiento):
        cara = list(map(lambda x: self.valor[x - 1], movimiento))    ## Sacamos las piezas que conforman la cara que estamos formando
        cara.insert(0, cara.pop())                                  ## Rotamos las posiciones de las piezas en sentido horario
        ## To-do
        # hay que rotar las letras dentro de cada posición tambien.  
        nuevo = list(map(lambda x: , self.valor))   ## Reincorporamos los valores desplazados a las posiciones que les corresponden y devolvemos un nuevo estado
        ## Guardando el movimiento realizado y el valor nuevo actual

        return estado([self.valor, movimiento])

