import os
import shutil

def ArrengeFolderContent(folder) -> bool:
    try:
        print(f'carpeta : {folder}')
        for filename in os.listdir(folder):
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
    except Exception as e:
        print(f'Function-Exception - Ocurrió un error: {e}, {type(e)}')