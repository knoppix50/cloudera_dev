# Automatizacion en Python
# Script para organizar una carpeta segun su contenido (imagenes, documentos, videos)
'''
Nota: En la carpeta actual hay una carpeta llamada backup_files que no utiliza el script.
En esa carpeta estan los ficheros iniciales. Copiad esos ficheros cuando hagais las pruebas
del script.
'''
import os
import shutil

#apunta al dicrectorio desde donde se lance el script
current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):
    if filename.endswith(('.jpg', '.png', '.gif')):
        if not os.path.exists("Images"): 
            os.makedirs('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)
        print('Images folder done')

    
    if filename.endswith(('.pdf', '.docx', '.doc', '.xls', '.txt' )):
        if not os.path.exists("Documents"): 
            os.makedirs('Documents')
        shutil.copy(filename, 'Documents')
        os.remove(filename)
        print('Documents folder done')

    
    if filename.endswith(('.apk', '.exe')):
        if not os.path.exists("Apps"): 
            os.makedirs('Apps')
        shutil.copy(filename, 'Apps')
        os.remove(filename)
        print('Apps folder done')

    if filename.endswith(('.mp4', '.wmv', '.avi')):
        if not os.path.exists("Videos"): 
            os.makedirs('Videos')
        shutil.copy(filename, 'Videos')
        os.remove(filename)
        print('Videos folder done')

print('all done')