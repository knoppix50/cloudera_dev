from math import sqrt
import math
#paradigma funcional python

#lista de num del 1 al 100
lista_100 = list(range(1,101)) # casting

def sumar_cinco_unidades(dato):
    return dato + 5

''' a todos y cada uno de los elementos de la lista_100
sumarle 5 unidades'''
#version clasica
nueva_lista = []
for item in lista_100:
    nueva_lista.append(sumar_cinco_unidades(item))
else:
    print(nueva_lista)

#version funcional
nueva_lista_funcional = list(map(sumar_cinco_unidades,lista_100))
print(nueva_lista_funcional)

#funciones lambda (anonimas)
restar_unidad = lambda x: x -1
nueva_lista_resta1 = list(map(restar_unidad,lista_100))
for item in nueva_lista_resta1:
    print("Desde lista:", item)
for item in map(restar_unidad, lista_100):
    print("Desde map:", item)
for item in map(lambda x: x - 1, lista_100):
    print("Desde lambda:", item)
# filtrado de datos
predicado = lambda x: x > 10 and x < 50
numeros_mayores_10_menores_50 = list(filter(predicado, lista_100))
print(numeros_mayores_10_menores_50)

#numeros_mayores_10_menores_50 realizar la raiz cuadrada (math)
'''
for item in numeros_mayores_10_menores_50:
    print(sqrt(item))
'''
lista_raiz_cuadra = list(map(math.sqrt, filter(predicado,lista_100)))
print(lista_raiz_cuadra)
print(list(map(lambda x: round(x,2),lista_raiz_cuadra)))
