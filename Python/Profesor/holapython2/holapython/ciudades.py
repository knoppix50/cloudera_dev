#funciones con docstring
def cargar_ciudades(l, data):
    '''Funcion que recibe una lista vacia l y la rellena con ciudades'''
    if data is not None:
        if l is not None and len(l) == 0:
            for ciudad in data:
                l.append(ciudad)

def mostrar_ciudades(l):
    '''Funcion que muestra por consola las ciudades recibidas a traves de la lista l'''
    for ciudad in l:
        print(ciudad)

def __anyadir_poblacion(ciudad, num_habitantes):
    return (ciudad, num_habitantes) 


def obtener_ciudades_con_datos_de_poblacion(l_ciudades):
    """Funcion que recibe una lista de ciudades a las cuales se les anyade el numero de habitantes"""
    import random

    data_ciudades = list()
    for ciudad in l_ciudades:
        data = __anyadir_poblacion(ciudad, random.randrange(1000,30000))
        data_ciudades.append(data)
    else:
        print("Proceso de carga de ciudades y poblaciones completado")
    
    return data_ciudades
