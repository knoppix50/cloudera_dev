def obtener_media_poblaciones(lista_poblaciones):
    sumatorio = 0
    for _, num_hab in lista_poblaciones:
        #sumatorio = sumatorio + num_hab
        sumatorio += num_hab
    
    media = sumatorio / len(lista_poblaciones)
    return media
    
