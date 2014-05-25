"""
ipadd.py
Nitaino

Genera direcciones de IP version 4 por haora.

"""

from libnitaino import analiza_serie, printea    

def procesa_ip(fun, cadena):
    """
    Toma una cadena en formato de una ip con series,
    Ejemplo:
      0-255.0.0.0
    I le applica fun cada combinacion possible de cada serie.
    
    # TODO: hazme mas funcional
    """
    
    serie1, serie2, serie3, serie4 = map(analiza_serie, cadena.split('.'))
    results = []    
    for i1 in serie1:
        for i2 in serie2:
            for i3 in serie3:
                for i4 in serie4:
                    results.append(fun('%s.%s.%s.%s' % (i1, i2, i3, i4)))
    return results
    

def genera_ips(cadena):
    """
    Toma una cadena en formato de una ip con series,
    i printea cada combinacion possible.
    """
    return procesa_ip(printea, cadena)

