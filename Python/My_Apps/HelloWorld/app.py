nombre = "Alfredo"
print(nombre)
print(type(nombre))

apellido1 = "Perez"
apellido2 = "Lopez"
#nombre = 90
print(type(nombre))

# snake
nombre_completo = nombre + " " + apellido1 + " " + apellido2
print(nombre_completo)

nombre_completo = f"{nombre}*{apellido1}*{apellido2}"
print(nombre_completo)

datos = nombre_completo.split("*")
datos.reverse()
print(datos)

#manipulacion de cadenas
primera_letra = nombre_completo[0]
ultima_letra = nombre_completo[-1]
print(f"La primera letra es {primera_letra} y la ultima es {ultima_letra}")
print(ultima_letra.upper())

nombres = ['Juan Ramirez', 'Ana Soler', 'Paco Lopez'] #lista vacia
print(len(nombres))

'''
Recorrer la lista nombres obteniendo solo el nombre de pila y convirtiendolo a mayusculas
'''
for nombre in nombres:
   print(nombre.split()[0].upper(), nombre.split()[1].lower())
   
print(nombre_completo)
print(nombre_completo.replace('*',' ')) #metodo rapido

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




