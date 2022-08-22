primeramente debemos crear en la ruta deseada una carpeta con el nombre "proyecto"

Para que el código funcione correctamente, se necesita abrir cada archivo.py 
y modificar las rutas de cada uno por la que estamos usando, inicialmente
se tiene la ruta "F:/" esta parte debemos reemplazarla por el lugar donde 
la carpeta proyecto esta siendo descomprimida, si se descomprimio en 
C en la carpeta modulo2, deberia ser "C:/modulo2/...." 

Para ayudar a la tarea de modificar las rutas de los archivos .py, se tomo la 
iniciativa de colocarlos en la parte superior como constantes, de tal manera
que sea facil cambiarlo

Una vez hecho esto, el programa cuenta con 2 partes:
1.- La parte de inicio, para ello abrimos el archivo "main.py" encontraremos
	una serie de pasos del 1 al 5, que debemos hacerlo uno por uno,
	hay que tener cuidado de esperar el tiempo necesario, ya que debemos 
	esperar a que descargue, comprima, etc.

2.- Una vez terminado todos los pasos procederemos a abrir "index.py"
	aqui se tiene el programa que crea, edita y elimina elementos
	del dataset y la base de fotos que se tiene, se usó "tkinter
	para el aspecto gráfico del programa.