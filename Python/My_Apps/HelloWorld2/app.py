#declaracion de variable nombre
nombre = "Juan"
primer_apellido = "Ramirez"
segundo_apellido = "Lopez"

#snake
#nombre_completo = nombre + " " + apellido 

nombre_completo = f"{nombre}*{primer_apellido}*{segundo_apellido}"
#print(nombre_completo)

datos = nombre_completo.split("*")

"""
datos.reverse()
print(datos)
"""
datos2 = reversed(datos)

'''
for dato in datos2:
    print(dato)
'''

print(datos2)

#manipulacio de cadenas
primera_letra = nombre_completo[0]
ultima_letra = nombre_completo[-1]

'''
print(f"La primera letra es {primera_letra} y la ultima es {ultima_letra}")
print(ultima_letra.lower())
'''

nombres = ['Juan Ramirez','Ana Soldevila','Jaime Lopez'] #lista

'''
Recorrer la lista nmbres obteniendo solo el nombre de pila y conviertindolo a mayuscula
'''
for nombre in nombres:
    '''
    print(nombre.split()[0].upper())
    print(nombre.split()[1].lower())
    '''
    print(nombre.split()[0].upper(), nombre.split()[1].lower())



print(nombre_completo)
#print(nombre_completo.replace('*',' '))

#print(len(nombres)) slicing
posicion_primera_aparicion_asterisco = nombre_completo.index('*')
nombre = nombre_completo[0:posicion_primera_aparicion_asterisco]
apellidos = nombre_completo[posicion_primera_aparicion_asterisco+1:]
print("Apellidos:" + apellidos)
pos_asterisco_entre_apellidos = apellidos.index('*')
print(pos_asterisco_entre_apellidos)
primer_apellido = apellidos[:pos_asterisco_entre_apellidos]
segundo_apellido = apellidos[pos_asterisco_entre_apellidos+1:]

print(nombre,primer_apellido, segundo_apellido)


print('_' * 60)
#tuplas
fiesta_sevilla = ("Sevilla", "Virgen del Rocio")
print(len(fiesta_sevilla))
for dato in fiesta_sevilla:
    print(dato)

#aceso a un elemento
nombre_ciudad = fiesta_sevilla[0]
nombre_fiesta = fiesta_sevilla[-1]
#fiesta_sevilla[0] = "Huelva" ERROR! Tupla no modificable

"""
Crear una funcion que reciba dos params: el nombre de una ciudad y el nombre de su fiesta prncipal
y devuelva una tupla con esos dartos y en ese orden
"""

def obtener_informacion_fiesta(ciudad, fiesta):
    return (ciudad, fiesta)


items = [12,2,3]
items[-1] = 4



