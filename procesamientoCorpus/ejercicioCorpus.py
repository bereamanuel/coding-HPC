# -*- coding: utf-8 -*-
"""
Created on Sunday, 3 July 2022

@author: manuelberea
"""

##Libraries

#Dataframe processing
import pandas as pd
import numpy as np

#Time processing
import time

#Multiprocessing utilities
import multiprocessing as mp
from multiprocessing import Pool

#Extract data
import nltk
from nltk.corpus import brown

## Functions

def make_texts():
        "This function make sentences from brown dataset"
        return [" ".join(np.random.permutation(sents)) for sents in brown.sents()]


def contarPalabrasBucle(data, columna = "text"):
    """
    Dado un dataset y una columna con string, devuelve el dataset modificado añadiendo el conteo de palbras de la columna dada.
    Input:
     - data: Dataframe(Pandas)
     - columna: String
    
    Output:
     - Dataframe (Pandas)
    
    Example:
        df.columns  => ["index", "text"]
        df = contarPalabras(df, "text")

        df.columns  => ["index", "text", "longitud"]
    """
    n = len(data)
    longitudes = []
    for i in range(n):
        longitudes.append(len(data.iloc[i][columna]))
    data["longitudBucle"] = longitudes
    return data


def contarPalabrasApply(data, columna = "text"):
    """
    Dado un dataset y una columna con string, devuelve el dataset modificado añadiendo el conteo de palbras de la columna dada.
    Input:
     - data: Dataframe(Pandas)
     - columna: String
    
    Output:
     - Dataframe (Pandas)
    
    Example:
        df.columns  => ["index", "text"]
        df = contarPalabras(df, "text")

        df.columns  => ["index", "text", "longitud"]
    """
    data["longitudApply"] = data[columna].apply(lambda x: len(x))
    return data


def partir(data, k):
    """
    Parte un dataframe en k trozos
    """
    trozos = []
    n = int(len(df)/k)
    for i in range(k):
        trozos.append(df.iloc[n*i:n*(i+1)])
        return trozos

## Start script
if __name__=="__main__":
    inicioScript = time.time()
    with open("output.txt", "a") as f:
        nltk.download("brown")
        
        print("Starting extract data", file=f)
        startData = time.time()
        df = pd.DataFrame({
            'text': make_texts() + make_texts() + make_texts() + make_texts()
        })
        finishData = time.time()
        print(f"Now the data is load. It took {finishData - startData} s", file=f)

        trozos = partir(df, 10)

        print("Secuential processing with for loop.", file=f)
        startBucleSecuential = time.time()
        bucle = contarPalabrasBucle(df)
        finishBucleSecuential = time.time()
        print(f"With for loop it takes {finishBucleSecuential - startBucleSecuential} s", file=f)
        print(bucle[:10], file=f)

        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ", file=f)

        print("Secuential processing with apply function.", file=f)
        startApplySecuential = time.time()
        bucle = contarPalabrasApply(bucle)
        finishApplySecuential = time.time()
        print(f"With for loop it takes {finishApplySecuential - startApplySecuential} s", file=f)
        print(bucle[:10], file=f)

        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ", file=f)
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ", file=f)
        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ", file=f)

        print(f"Pool processing with {int(mp.cpu_count()//2)} cores.", file=f) 
        with mp.Pool(int(mp.cpu_count()//2)) as p:
            
            startBuclePool = time.time()
            nuevo = pd.concat(p.map(contarPalabrasBucle, trozos) , ignore_index= True)
            finishBuclePool = time.time()
            print(f"With for loop it takes {finishBuclePool - startBuclePool} s", file=f)
            print(nuevo[:10], file=f)

        print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ", file=f)

        with mp.Pool(int(mp.cpu_count()//2)) as p:
            startApplyPool = time.time()        
            nuevo = pd.concat(p.map(contarPalabrasApply, trozos) , ignore_index= True)
            finishApplyPool = time.time()
            print(f"With Apply it takes {finishApplyPool - startApplyPool} s", file=f)
            print(nuevo[:10], file=f)

        print(f"Finish script in {time.time() - inicioScript}", file=f)