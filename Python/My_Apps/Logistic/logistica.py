def __ir_a_destino(destino):
    return True

def transportar_mercancias(paquetes, destinos, numero_entregas_por_destino):

    assert len(destinos) > 0, "Sin destinos a los que llevar la mercancia"

    while len(destinos) > 0:
        if __ir_a_destino(destinos[0]):
            paquetes = paquete[]
            destinos.pop(0)
    else:
        print("Reparto concluido v1")