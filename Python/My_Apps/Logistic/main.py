import mercancias as merca
import logistica as log

#mercancia = list() #lista vacia
paquetes = list() 

def empaquetar_mercancias(mercas):
    paquetes = []
    i = 0
    j = 5
    numero_paquetes = len(mercas) // 5 
    for k in range(numero_paquetes):
        paquete = mercas[i:j]
        paquetes.append(paquete)
        print(f"Paquete numero {k+1} ha sido procesado. Info {paquete}")
        i = i + 5
        j = j + 5
        
    
    return paquetes
        

if __name__ == "__main__":

    print(merca.cargar_mercancias()[:5]) #imprime las 5 primeras
    print(merca.cargar_mercancias()[-5:]) #imprime las 5 ultimas
    paqueteria = empaquetar_mercancias(merca.cargar_mercancias())
    log.transportar_mercancias(paqueteria, ['Al Campo Gourmet', 'El Corte Ingles'])

