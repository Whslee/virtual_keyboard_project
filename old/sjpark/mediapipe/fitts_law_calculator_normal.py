#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, sys
import math as m
import random
import string
import pandas as pd

# In[ ]:


# key width equal to 1key
keyWidth = 1.0
# ABC keyboard layout
layout = {'o': (0, 0, 0), 'a': (1, 0, 0), 'r': (2, 0, 0), 'n': (0, 1, 0), 't': (1, 1, 0), 'e': (2, 1, 0), 'i': (0, 2, 0), 's': (1, 2, 0),  'h': (2, 2, 0), 'f': (0, 0, 1), 'm': (1, 0, 1), 'p': (2, 0, 1), 'u': (0, 1, 1), 'l': (1, 1, 1), 'd': (2, 1, 1), 'g': (0, 2, 1), 'c': (1, 2, 1), 'w': (2, 2, 1), 'j': (0, 0, 2), 'b': (1, 0, 2), 'x': (2, 0, 2), 'q': (0, 1, 2), 'y': (1, 1, 2), 'v': (2, 1, 2), 'z': (0, 2, 2), 'k': (1, 2, 2)}
#key coordinate for a 3 rows by 3 column keyboard
cord = [[(x + keyWidth/2.0, y + keyWidth/2.0) for x in range(3)] for y in range(3)]


# In[ ]:


# Make a Digram Table , which is a dictionary with key format (letter_i,letter_j) to its Pij
def makeDigramTable(data_path):
    fp = open(data_path)
    line = fp.readline()
    total = 0 
    count = 1
    dict = {}
    tbl = {}

    while line:

        for i in range(len(line) -1):
            pair = line[i].lower() + ',' + line[i+1].lower()
            if pair in dict:
                dict[pair] = (dict[pair][0] + count, line[i].lower(), line[i+1].lower())

            if pair not in dict:
                dict[pair] = (count, line[i].lower(), line[i+1].lower())
            
            total = total + count
        line = fp.readline()

    fp.close()

    for k, v in dict.items():
        dict[k] = (v[0], v[1], v[2], v[0] /total)
    
    return dict


# In[ ]:


def FittsLaw(W,D):
    #implement the Fitt's Law based on the given arguments and constant
    a = 0.083
    b = 0.127
    
    mt = a + b*(m.log2(D/W + 1))
    return mt


# In[ ]:


def FastType(W,D):
    b = 0.127
    mt = b*(m.log2(D/W +1))
    return mt


# In[ ]:


def calculateDistance(a,b):
    x1,y1 = cord[a[0]][a[1]]
    x2,y2 = cord[b[0]][b[1]]
    return m.sqrt(pow((y2-y1),2) + pow((x2 - x1),2))


# In[ ]:


def computeAMT(layout, tbl):
    t1 = 0
    # Compute the average movement time
    for val in tbl.values():
        mt = FittsLaw(keyWidth, calculateDistance(layout[val[1]], layout[val[2]]))
        t1 += mt*val[3]
    return t1


# In[ ]:


def computeAS(layout, tbl):
    s = 0
    t2 = 0
    # using parameter in the paper
    click = 0.488
    repeat = 1.8
    layer = 0.37
# Compute the S(k) and then get value of total time(Ttot)
    for val in tbl.values():
        if layout[val[1]][2]==layout[val[2]][2]:
            if val[1] == val[2]:
                s = click + repeat
            if val[1] != val[2]:  
                s = click
        if layout[val[1]][2] != layout[val[2]][2]:
            s = click+layer
        t2 += val[3]*s
    return t2


# In[ ]:


main_dict = makeDigramTable('merge.txt')
t1 = computeAMT(layout, main_dict)
t2 = computeAS(layout,main_dict)
T_tot = t1 + t2
print(t1)
print(t2)
print(T_tot)

