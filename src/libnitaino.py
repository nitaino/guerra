"""
libnitaino.py
Nitaino

Funciones que se pueden usar en todo y otros
lugares.

"""
from string import digits


def collecion_a_numeros(cadenas):
    """
    Con una collecion, trata
    de convertirlas en una cadena de numeros
    
    """
    
    return map(int, cadenas)

