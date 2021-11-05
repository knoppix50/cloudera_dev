# Automatizacion en Python
# Script para organizar una carpeta segun su contenido (imagenes, documentos, videos)
'''
La idea es organizar la carpeta target (cajonDesastre) y que funcione igual que la
version 1. 
Esta version presenta un bug
'''
import os
import shutil
import sys
from functions import ArrengeFolderContent


if __name__ == "__main__" :
    if len(sys.argv) == 2:
        try:
            argvDir = sys.argv[1]
            #print(type(argvDir)) comprobacion
            target_dir = os.path.dirname(argvDir)
            #print(target_dir)
            ArrengeFolderContent(target_dir)
            if ArrengeFolderContent == True:
                print('all done')
        except Exception as e:
            print(f'Main-Exception - Ocurrió un error: {e}, {type(e)}')