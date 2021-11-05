import ciudades


if __name__ == "__main__":
    print("Este es el programa principal/punto de entrada")
    lista_ciudades = list()
    ciudades.cargar_ciudades(lista_ciudades)
    ciudades.mostrar_ciudades(lista_ciudades)