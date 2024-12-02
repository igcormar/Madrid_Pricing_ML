import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from scipy.stats import f_oneway, pearsonr
import seaborn as sns
import matplotlib.pyplot as plt


def filtrar_columnas(df, columns_to_exclude):
    '''
    Creamos una pequeña función para ir filtrando las columnas restantes.
    '''
    # Crear una lista de columnas restantes
    columns_remaining = [col for col in df if col not in columns_to_exclude]
    # Filtrar el DataFrame para incluir solo las columnas restantes
    df_remaining = df.loc[:, ~df.columns.isin(columns_to_exclude)]
   
    return df_remaining


def obtener_datos_faltantes(df):
    '''
    Creamos una función para ir ordenando las features según los datos faltantes que tengan.
    '''

    # Calcular el total de datos faltantes
    total = df.isnull().sum().sort_values(ascending=False)
    # Calcular el porcentaje de datos faltantes
    percent = (df.isnull().sum() / df.isnull().count()).sort_values(ascending=False)
    # Combinar ambos en un DataFrame
    missing_data = pd.concat([total, percent], axis=1, keys=['Total Missing Data', 'Nulls Percent'])

    return missing_data



def describe_df(df):
    '''
    Esta función muestra información específica del DF original. 
    Esa información será: el tipo de objeto, el % de valores nulos o missings,
    los valores únicos y el % de cardinalidad de cada columna del DF original.

    Argumentos:
    df (pd.DataFrame): DF original sobre el que queremos recibir la información.

    Retorna:
    pd.DataFrame: Df con la información específica.
    '''

    # se crea un diccionario con la columna que va a estar fija
    # Y después se añaden las columnas del DF original

    dict_col = {'COL_N': ['DATA_TYPE', 'MISSINGS (%)', 'UNIQUE_VALUES', 'CARDIN (%)']}

    # Fórmula para calcular el porcentaje de nulos
    na_ratio = ((df.isnull().sum() / len(df))*100)

    # Se añade al diccionario como clave el nombre de las columnas, y como valores
    # la información del describe
    for col in df:
        dict_col[col] = [df.dtypes[col], na_ratio[col], len(df[col].unique()), round(df[col].nunique()/len(df)*100,2)]

    #  Se crea el DF.describe
    df_describe = pd.DataFrame(dict_col)

    return df_describe



