from proyecto.start import *
import os


print('Consola de inicio del dataset')
print('#############################')
print('1.- Crear credenciales')
print('2.- Descarga el archivo de kaggle')
print('3.- Descomprimir archivo')
print('4.- Ordenar imágenes en una carpeta')
print('5.- Crear data set a partir de las imagenes')
print('6.- Salir')
print('#############################')

select = 2
select = int(select)
KAGGLE_PATH = "F:/proyecto/descargas"

while select < 6:
    
    select = input()
    select = int(select)    
    
    if select == 1:
        start.credenciales()
        print('credenciales creadas con éxito')
        
    elif select == 2:
        #Estafuncion descarga desde kaggle el paquete.
        os.chdir(KAGGLE_PATH)   
        print('esperar unos minutos hasta que termine de descargar')
        #!kaggle datasets download -d tawsifurrahman/covid19-radiography-database
        print('descarga terminada')
        
    elif select == 3:
        print('esperar unos minutos hasta que termine de descomprimir')
        start.descompresion()
        print('Descompresión terminada')
        
    elif select == 4:
        #este archivio crea en proyecto/imagenes una copia train y test con las imagenes ordenadas, esperar algo de 5 min
        print('esperar unos minutos hasta que termine de ordenar')
        sort.create_dir()
        print('Finalizado')
        
    elif select == 5:
        dataset.create()
        print('Archivo creado con éxito')
        
    else:
        print('Saliendo')
        
    