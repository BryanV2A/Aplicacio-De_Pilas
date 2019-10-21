# Implementación de una pila para resolver el problema:

""" De escribir un método para determinar si una secuencia de caracteres de entrada es de la forma:
	X & Y.

    Siendo X una cadena de caracteres y Y la cadena inversa.
    El carácter & es el separador. """

class aplicacionDePilas:

    __PilaUno = ["B", "R", "Y", "A", "N", ]
    __PilaDos = ["N", "A", "Y", "R", "B", ]
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