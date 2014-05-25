"""
libnitaino.py
Nitaino

Funciones que se pueden usar en todo y otros
lugares.

"""
from string import digits


def analiza_serie(cadena):
    """
    Convierte una cadena en formato n1-n2 a una serie
    de numeros, Opcionalmente tambien se puede a~adir un
    tercer numero n1-n2-n3, que representa el pazo entre
    cada elemento.
    """
    # la cadena no puede estar bacia ni contenere letras que no sean '-'
    # solo numeros tambien checkea que la cadena no sea ''
    
    if ('-' not in cadena):
        # solo un numero sin '-' regresa una collecion con
        # solo el numero
        return collecion_a_numeros([cadena])
    else:
        return range(*(collecion_a_numeros(cadena.split('-'))))


def printea(cadena):
    """
    Como print pero una funcion.
    """
    print(cadena)
    
    return cadena

def collecion_a_numeros(cadenas):
    """
    Con una collecion, trata
    de convertirlas en una cadena de numeros
    
    """
    
    return map(int, cadenas)

