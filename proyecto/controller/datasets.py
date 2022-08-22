from re import U
import pandas as pd
import os

'''Se debe definir aquí la ruta del proyecto, inicialmente se tiene en el disco F, si se tiene el archivo
en otro lugar, se debe agregar dicha direccion por ejemplo: si se tiene en el disco C, en la carpeta programas sería
'C:/programas/proyecto/codigo/dataset.csv, lo mismo para el train path'''

PATH_CSV = 'F:/proyecto/codigo/dataset.csv'
PATH_TRAIN = 'F:/proyecto/imagenes/train_data/'


def insert(tupla):
    df1 = pd.read_csv(PATH_CSV)
    df2 = pd.DataFrame([tupla])
    df1.columns = ['Nombre','Formato','Categoria','URL']
    df2.columns = ['Nombre','Formato','Categoria','URL']  
    df = pd.concat([df1,df2])
    df.to_csv(PATH_CSV, index=False)
    
def delete(url):
    file_path = url
    df = pd.read_csv(PATH_CSV)
    df = df.drop(df[df.URL == file_path].index)   
    df.to_csv(PATH_CSV, index=False)

def update(url,tupla):
    delete(url)
    insert(tupla)