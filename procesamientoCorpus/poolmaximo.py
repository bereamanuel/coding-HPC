#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 21:04:18 2021

@author: mluisadiez
"""
import multiprocessing as mp
import numpy as np
from time import time
from functools import partial

def cuanto(minimo,maximo,row):
    count=0
    for n in row:
       if minimo<=n<=maximo:
        count+=1
    return count

if __name__=="__main__":
    mp.freeze_support()
    print(mp.cpu_count())
    np.random.RandomState(100)
    arr=np.random.randint(0,10,size=[200000000,5])
    data=arr.tolist()
    
    results=[]
    inicio=time()
    for row in data:
        results.append(cuanto(minimo=4,maximo=8,row=row))
    print("secuencial")
    print(time()-inicio)
    print(results[:10])
    
    pool=mp.Pool(mp.cpu_count())
    inicio=time()
    
   
    nuevos=partial(cuanto,4,8)
    results=pool.map(nuevos, data )
    print("paralelo")
    print(time()-inicio)
    pool.close()
    print(results[:10])