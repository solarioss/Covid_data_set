import json
import os
import zipfile

'''Aquí se debe pegar la dirección de la carpeta que se tiene tomando en cuenta la dirección donde está pegada'''

KAGGLE_PATH = "F:/proyecto/descargas"
API_PATH = "F:/proyecto/codigo"


'''En esta parte se debe colocar las credenciales de su cuenta, acutalmente se tiene una, pero para evitar
problemas, se debe integrar la suya'''
def credenciales():    
    #esta funcion genera las credenciales de kaggle para iniciar culquier operacion
    os.mkdir(KAGGLE_PATH)
    api_token = {"username":"erickpc","key":"c414dbe542675528e1adaa8adc0dbe31"}
    with open(API_PATH + 'kaggle.json', 'w') as file:
        json.dump(api_token, file)
        

    

def descompresion():
    if not os.path.exists('./imagenes'):
      os.makedirs('imagenes')
    with zipfile.ZipFile(KAGGLE_PATH + "/covid19-radiography-database.zip", 'r') as zip_ref:
        zip_ref.extractall(KAGGLE_PATH + '/images')


