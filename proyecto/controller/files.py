
from os import listdir
import shutil
import os
import pandas as pd


PATH_TRAIN = 'F:/proyecto/imagenes/train_data/'
categories = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]
PATH_CSV = 'F:/proyecto/codigo/dataset.csv'

def copy_image(categoria, archivo):
    destination = PATH_TRAIN + categoria + '/'
    source = archivo
    idx = len(listdir(destination))
    idx += 1
    filename = archivo
    dir, fmt = filename.split(".")
    name = categoria+'-'+str(idx)
    destination = destination + name + '.' + fmt
    shutil.copy(source, destination)
    return [name, fmt, categoria, destination]


def delete_image(url):
    file_path = url
    
    
    if os.path.isfile(file_path):
        os.remove(file_path)
        print("La imagen fue eliminada")
    else:
        print("La imagen no existe")
        
def update(categoria,url):
    
    df = pd.read_csv(PATH_CSV)
    urllist = df['URL'].to_numpy()    
    try:        
        if not categoria in categories:
            raise NotClass            
        if url in urllist:
            raise URLError
        
    except NotClass:
        print("la clase no existe")
        print()
    except URLError:
        print("la imagen ya esta en la base de datos")
        print()
    
    
    tupla=copy_image(categoria=categoria,archivo=url)
    delete_image(url=url)
    return tupla







class NotClass(Exception):
    def __init__(self, message="La clase no existe"):            
            self.message = message
            super().__init__(self.message)
            
class URLError(Exception):
    def __init__(self, message="la url ya existe"):            
            self.message = message
            super().__init__(self.message)
