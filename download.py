import numpy as np
import pandas as pd
import urllib.request
from tqdm import tqdm

# Leemos el dataset de entrenamiento para el preprocesamiento

df_train = pd.read_csv(
    "Train_GCC.tsv", sep='\t', header=None)
df_train.columns = ["descrption", "url"]


def url_to_jpg(i, url, file_path):

    filename = 'image-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))

    return None


FILE_PATH_TRAIN = 'train/'

# RECORREMOS EL DATAFRAME DE TRAIN
tot_error_train = 0

for i in tqdm(range(df_train.shape[0])):
    aux = df_train.iloc[i]
    try:
        url_to_jpg(i, aux.url, FILE_PATH_TRAIN)
    except:
        tot_error_train += 1
