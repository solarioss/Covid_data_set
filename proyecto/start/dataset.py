import pandas as pd
import os


def create():
    TRAINSET_PATH = "F:/proyecto/imagenes/train_data"
    CSV_PATH = 'F:/proyecto/codigo/dataset.csv'
    
    
    categories = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]

    nombre = []
    formato = []
    categoria = []
    URL = []

    for category in categories:
        actual_path = TRAINSET_PATH + '/' + category
        a = os.listdir(actual_path)
        df = pd.DataFrame(a)

        for i in range(len(df)):
            nom, form = df.iloc[i][0].split(".")
            nombre.append(nom)
            formato.append(form)
            categoria.append(category)
            link = TRAINSET_PATH + '/' + category + '/' + df.iloc[i][0]
            URL.append(link)

    df = pd.DataFrame(nombre)
    df.columns = ['Nombre']
    df['Formato'] = formato
    df['Categoria'] = categoria
    df['URL'] = URL

    df.to_csv(CSV_PATH, index=False)
