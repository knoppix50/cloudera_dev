import sys

import ciudades as c
import estadistica as estad

def recoger_info_ciudades(ciudades):
    """Funcion que muestra la seccion de parametros relativa ala ciudades"""
    for ciudad in ciudades:
        print(ciudad)

def tratar_parametro_ciudades(info):
    data = None
    if info is not None and len(info) > 0:
        data = info.split("*")
    
    return data 

if __name__ == "__main__":
    
    """ Version clasica
    if len(sys.argv) != 3:
        sys.exit(1)
    """
    try:
        
        assert len(sys.argv) == 3, "Faltan argumentos"
        
        print("Este es el programa principal / punto de entrada")

        lista_ciudades = list() #[]

        #recogida de ciudades
        ciudades = tratar_parametro_ciudades(sys.argv[2])
        c.cargar_ciudades(lista_ciudades, ciudades)
        #recogida parametro
        ciudades = c.obtener_ciudades_con_datos_de_poblacion(lista_ciudades)
        interruptor = int(sys.argv[1])
        #gestion del valor del parametro
        if interruptor == 1:
            c.mostrar_ciudadess(ciudades)
            print(f"La media de las poblaciones tratadas es {round(estad.obtener_media_poblaciones(ciudades),2)}")
    
    except AssertionError as asex:
        print(asex)
    except:
        print("Error general")