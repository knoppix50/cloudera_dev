
productos = ["Chuleton gallego", "Costillas bbq", "Pollo corral", "Jamon 5J"]

def cargar_mercancias():
    import random
    mercancias = list()
    for i in range(1,21):
        mercancia = (i, random.choice(productos)) #creacion de tupla mercancia
        mercancias.append(mercancia) #lista de tupla mercancia
    return mercancias






