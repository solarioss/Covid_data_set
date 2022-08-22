import os
import shutil
import pandas as pd

TRAINSET_PATH = "F:/proyecto/imagenes/train_data"
TESTSET_PATH = "F:/proyecto/imagenes/test_data"
ORIGIN_PATH="F:/proyecto/descargas/images/COVID-19_Radiography_Dataset"
categories = ["COVID","Lung_Opacity","Normal","Viral Pneumonia"]


def create(target_path):
    #Funcion privada de apoyo que crea las carpetas de una ruta especificada
    if not os.path.exists(target_path):
        os.makedirs(target_path)   
    for idx, category in enumerate(categories):    
        a= os.listdir(ORIGIN_PATH + '/'+category + '/images')
        df= pd.DataFrame(a)
        os.makedirs(target_path + '/'+category)   
        for i in range (len(df)):
            shutil.copy(ORIGIN_PATH + '/'+category + '/images/' + df.iloc[i][0], target_path + '/' + category)  


def create_dir():
    #Esta funcion usa la funcion create para aplicarla a ambas rutas que se tiene
    create(TRAINSET_PATH)
    create(TESTSET_PATH)
    
    

   
 
