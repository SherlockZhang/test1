# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:54:45 2020

@author: xinzh
"""

import numba as nb
import timeit
import numpy as np

@nb.jit()
def nb_sum(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s

def py_sum(a):
    s = 0
    for i in range(len(a)):
        s += a[i]
    return s


a = np.linspace(0,100,10**6)


