#funciones
def cargar_ciudades(l):
    if l is not None:
        l.append("Barcelona")
        l.append("Madrid")
        l.append("Oviedo")

def mostrar_ciudades(l):
    for ciudad in l:
        print(ciudad)