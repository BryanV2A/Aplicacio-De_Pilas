class aplicacionDePilas:

    __PilaAux = []
    __listaPila = []

    def __init__(self):
        self.__listaPila = []

    #Método encargado de insertar valores en una pila
    def Insertar(self, elemento):
        self.__listaPila.append(elemento)

    #Método que verifica si la pila se encuentra vacía
    def PilaVacia(self):
        if len(self.__listaPila) == 0:
            return True
        else:
            return False

    #Método para extraer o remover el ultimo elemneto de la pila
    def Quitar(self):
        #Condicional para verificar si la pila se encuenta vacía sí no para remover el elemento
        if self.PilaVacia():
            return False
        else:
            elemento = self.__listaPila.pop()
            return elemento

    #Método para obtener el tamaño de la pila insertada
    def getTamPila(self):
        return len(self.__listaPila)

    #Método encargado de comparar las pilas y generar un resultado booleano
    def Comparar(self, PilaAux, PilaDos):
        while True:
            if (len(PilaAux) == len(PilaDos)):
                for a in range(0, len(PilaAux)):
                    if (PilaAux[a] != PilaDos[a]):
                        return False
            else:
                return False
            return True

#Método que accede a la clase aplicacionDePilas y así realizar la comparacion
def main():
    pila = aplicacionDePilas()

    PilaAux = []
    X = ["E", "R", "R", "O", "R"]
    Y = ["R", "O", "R", "R", "3"]

    #Ciclo para ingresar la pila "X"
    for y in range(0, len(X)):
        pila.Insertar(X[y])

    #Ciclo para obtener la inversa de "X" y guardarla en una pila Auxiliar
    for x in range(0, pila.getTamPila()):
        PilaAux.append(pila.Quitar())

    #Mensaje para mostrar el resultado
    print(pila.Comparar(PilaAux, Y))
    return 0

#Sentencia para acceder al método main que es el encargado de acceder a la clase aplicacionDePilas
if __name__ == '__main__':
    main()