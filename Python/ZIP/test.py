
diccionario = dict()

#creacion del dicionario
"""
diccionario['python'] = 'Lenguaje de programacion que mola'
diccionario['java'] = 'Lenguaje de programacion que mola un poco menos que python'
diccionario['kotlin'] = 'Lenguaje de programacion que mola mucho'
diccionario['typescript'] = 'Lenguaje de programacion que es mejor que javascript'
"""

topics = ('python','kotlin')

diccionario['python'] = ['Lenguaje de programacion que mola']
diccionario['java'] = ['Lenguaje de programacion que mola un poco menos que python']
diccionario['kotlin'] = ['Lenguaje de programacion que mola mucho']
diccionario['typescript'] = ['Lenguaje de programacion que es mejor que javascript']


#encuesta
def realizar_encuesta(topics, data):
    for topic in topics:
        opinion = input(f'Opinion sobre {topic}')
        data[topic].append(opinion)

def mostrar_opiniones(topic, data):
    opiniones = data.get(topic,None)
    if opiniones is not None:
        for opinion in opiniones:
            print(opinion)

def mostrar_todas_las_opiniones(data):

    """
    for topic, _ in data.items():
        mostrar_opiniones(topic, data)
    """
    todas_las_opiniones = data.values()
    for opiniones_por_topic in todas_las_opiniones:
        for opinion in opiniones_por_topic:
            print(opinion)


topic_de_trabajo = 'kotlin'
realizar_encuesta((topic_de_trabajo,), diccionario)
print('*' * 60)
mostrar_opiniones(topic_de_trabajo, diccionario)
print('_' * 60)
mostrar_todas_las_opiniones(diccionario)
print('*' * 60)





""" try:
    opinion_kotlin = diccionario['kotlin']
    print(f"La opinion sobre kotlin de este usuario es {opinion_kotlin}")
except KeyError as kex:
    print(f"Error de lectura del diciconario:{kex}")
except:
    print("Error general de dicionario") """

#version 2
opinion_kotlin = diccionario.get('kotlin', None)
if opinion_kotlin is not None:
    #print(f"La opinion sobre kotlin de este usuario es {opinion_kotlin}")
    pass

#version 3
clave_a_buscar = 'kotlin'
if clave_a_buscar in diccionario:
    '''
    print(f"""La opinion sobre kotlin de
                este usuario es {diccionario[clave_a_buscar]}""")
    '''

    print("La opinion sobre kotlin de" \
            f"este usuario es {diccionario[clave_a_buscar]}")

    
def obtener_info_lenguaje(topic:str, dicc:dict) -> str:
    assert topic is not None, "No existe topic"

    if topic in dicc:
        return dicc[topic]
    else:
        return None

#preguntar al usuario por el topic
topic = input('Escriba topic (kotlin,python,java,typescript):')
try:
    hay_info = obtener_info_lenguaje(topic, diccionario)
    
    """ if hay_info:
        print(hay_info)
    else:
        print("Sin informacion sobre este topic") """
    print(hay_info if hay_info else "Sin informaci0n sobre este topic")

except AssertionError as aex:
    print(aex)

