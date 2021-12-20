class estado:
    final = [1, 2, 3, 4, 5, 6, 7, 8]

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
