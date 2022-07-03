#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:42:20 2021

@author: mluisadiez
"""
from multiprocessing import Pool
import numpy as np

def media(l):
    return np.mean(l)

if __name__ == '__main__':
    listas=[[1, 2, 3],[5, 2, 7],[4, 4, 4]]
    with Pool(5) as p:
        print(p.map(media, listas))