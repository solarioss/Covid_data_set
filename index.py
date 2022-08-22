from contextlib import nullcontext
from proyecto.controller import files
from proyecto.controller import datasets
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import tkinter as tk
import pandas as pd
from PIL import ImageTk, Image


DATAFRAME_PATH = 'F:/proyecto/codigo/dataset.csv'
class Product:



    def __init__(self, window):
        # Initializations
        self.wind = window
        self.wind.title('Proyecto Final')

        # Insert Button
        Button(self.wind, text='Registrar nueva imagen', command=lambda: self.insert()).grid(
            row = 0, column = 0, sticky = W + E, pady = 10)

        # Table
        columns = ('name', 'format', 'category', 'url')
        self.tree = ttk.Treeview(self.wind, columns = columns, show = 'headings')
        self.tree.grid(row = 1, column = 0, columnspan = 1)
        self.tree.bind('<<TreeviewSelect>>', self.item_selected)

        # define headings
        self.tree.heading('name', text='Nombre')
        self.tree.column('name', minwidth = 0, width = 100, stretch = NO)
        self.tree.heading('format', text = 'Formato')
        self.tree.column('format', minwidth = 0, width = 55, stretch = NO)
        self.tree.heading('category', text='Categoria')
        self.tree.column('category', minwidth = 0, width = 100, stretch = NO)
        self.tree.heading('url', text = 'URL')
        self.tree.column('url', minwidth = 0, width = 300, stretch = NO)

        # define scrollbar
        scrollbar = ttk.Scrollbar(
            self.wind, orient=tk.VERTICAL, command = self.tree.yview)
        self.tree.configure(yscroll = scrollbar.set)
        scrollbar.grid(row = 1, column = 1, sticky = 'ns')

        self.fill_rows()

    def fill_rows(self):
        # cleaning Table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        # Filling the Rows
        df = pd.read_csv(DATAFRAME_PATH)
        rows = df.to_numpy().tolist()
        for row in rows:
            self.tree.insert('', tk.END, values = row)

    def insert(self):
        self.insert_wind = Toplevel()
        self.insert_wind.title = 'Registrar'
        self.insert_wind.geometry('600x350')
        self.isOpen = FALSE
        Button(self.insert_wind, text='Abrir Imagen', command = lambda: self.abrirArchivo(
        )).grid(row = 0, column = 0, pady = 20, padx = 20)
        self.var = IntVar()
        self.var.set(0)
        Radiobutton(self.insert_wind, text = "COVID",
                    variable=self.var, value = 0).grid(row = 1, column = 0)
        Radiobutton(self.insert_wind, text = "Lung_Opacity",
                    variable=self.var, value = 1).grid(row = 2, column = 0)
        Radiobutton(self.insert_wind, text = "Normal",
                    variable=self.var, value = 2).grid(row = 3, column = 0)
        Radiobutton(self.insert_wind, text = "Viral Pneumonia",
                    variable=self.var, value = 3).grid(row = 4, column = 0)

        Button(self.insert_wind, text='Registrar', command=lambda: self.registrar()).grid(
            row = 5, column = 0, pady = 20, padx = 20)

        self.insert_wind.mainloop()

    def registrar(self):
        categories = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]
        if (self.isOpen):
            self.insert_wind.destroy()
            tupla = files.copy_image(
                archivo = self.archivo_abierto, categoria=categories[self.var.get()])
            datasets.insert(tupla)
            self.fill_rows()
        else:
            showinfo(message = 'seleccione un archivo imagen primero')

    def eliminar(self, url):
        self.view_wind.destroy()
        files.delete_image(url)
        datasets.delete(url)
        self.fill_rows()

    def item_selected(self, event):
        # data item selected
        try:
            self.name = self.tree.item(self.tree.selection())['values'][0]
            self.format = self.tree.item(self.tree.selection())['values'][1]
            self.category = self.tree.item(self.tree.selection())['values'][2]
            self.url = self.tree.item(self.tree.selection())['values'][3]
        except IndexError as e:
            return

        self.view_wind = Toplevel()
        img = PhotoImage(file=self.url)
        Label(self.view_wind, image=img).grid(
            row = 0, column = 0, rowspan = 9, padx = 20, pady = 20)
        Label(self.view_wind, text = 'Nombre:').grid(row = 0, column = 1)
        Label(self.view_wind, text=self.name).grid(row = 1, column = 1)
        Label(self.view_wind, text='Categoria:').grid(row = 2, column = 1)
        categories = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]
        self.cat = IntVar()
        self.cat.set(categories.index(self.category))
        Radiobutton(self.view_wind, text = "COVID",
                    variable=self.cat, value = 0).grid(row = 3, column = 1)
        Radiobutton(self.view_wind, text = "Lung_Opacity",
                    variable=self.cat, value = 1).grid(row = 4, column = 1)
        Radiobutton(self.view_wind, text = "Normal",
                    variable=self.cat, value = 2).grid(row = 5, column = 1)
        Radiobutton(self.view_wind, text = "Viral Pneumonia",
                    variable=self.cat, value = 3).grid(row = 6, column = 1)

        Button(self.view_wind, text = 'Modificar',
               command = lambda: self.modificar(self.url)).grid(row = 7, column = 1)

        Button(self.view_wind, text='Eliminar',
               command = lambda: self.eliminar(self.url)).grid(row = 8, column = 1)
        self.view_wind.mainloop()

    def modificar(self, url):
        categories = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]
        if (categories[self.cat.get()] == self.category):
            showinfo(message = 'no selecciono categoria distinta')
        else:
            self.view_wind.destroy()
            tupla = files.update(categoria=categories[self.cat.get()], url = url)
            datasets.update(url = url, tupla = tupla)

    def abrirArchivo(self):
        global imagen
        self.archivo_abierto = fd.askopenfilename(initialdir="/",
                                                  title="Seleccione archivo", 
                                                  filetypes=(("png files", "*.png"),
                                                             ("all files", "*.*")))
        print(self.archivo_abierto)
        if (self.archivo_abierto):
            imagen = tk.PhotoImage(file=self.archivo_abierto)
            lbImagen = tk.Label(self.insert_wind, image = imagen).place(
                relx = .5, rely = .1, relwidth = .4, relheight = .5)
            lbPath = tk.Label(self.insert_wind, text=self.archivo_abierto).grid(
                row = 0, column = 1)
            self.isOpen = TRUE


if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
