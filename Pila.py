# Implementación de una pila para resolver el problema:

""" De escribir un método para determinar si una secuencia de caracteres de entrada es de la forma:
	X & Y.

    Siendo X una cadena de caracteres y Y la cadena inversa.
    El carácter & es el separador. """

class aplicacionDePilas:

    __PilaUno = ["B", "R", "Y", "A", "N", ]
    __PilaDos = ["N", "A", "Y", "R", "B", ]
    __PilaAux = []
    __tamPila = int(0)
    __cima = 0