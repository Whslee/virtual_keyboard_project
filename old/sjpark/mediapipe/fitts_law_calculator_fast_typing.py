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
def makeDigramTable(data_path, layout):
    fp = open(data_path)
    line = fp.readline()
    total = 0 
    count = 1
    dict = {}
    start_char = 0
   
    typing_weight = 0
    click_depth = 0.488
    change_layer = 0.37
    repeat = 1.8

    while line:

        line = line.strip()
        line = line.lower()
        if start_char != 0:
            pair = start_char + ',' + line[0]
            # same_layer
            if layout[start_char][2] == layout[line[0]][2]:
                if calculateDistance(layout[start_char], layout[line[0]]) == 0:                                             # same_key
                    total_weight = repeat
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, start_char, line[0], total_weight)
                elif 0 < calculateDistance(layout[start_char], layout[line[0]])/keyWidth <= m.sqrt(2):                          # neighborhood_key
                    total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]]))
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, start_char, line[0], total_weight)
                else:
                    total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth # normal_case
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, start_char, line[0], total_weight)
                
            # different_layer
            else:
                if layout[start_char][1] == layout[line[0]][1]:
                    if layout[start_char][0] == layout[line[0]][0]:                                                         # same_x_y_cord
                        total_weight = click_depth + change_layer
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, start_char, line[0], total_weight)
                            
                    else:                                                                                                  # different_x_y_cord
                        total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth + change_layer 
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, start_char , line[0], total_weight)  
                else:
                    total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth + change_layer 
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, start_char , line[0], total_weight)                           

            total += count
            start_char = 0

        for i in range(len(line) -1):
            pair = line[i] + ',' + line[i+1]
  
            # same_layer
            if layout[line[i]][2] == layout[line[i+1]][2]:                                                             
                if calculateDistance(layout[line[i]], layout[line[i+1]])/keyWidth == 0:                                    # same_key
                    total_weight = repeat
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, line[i], line[i+1], total_weight)
                elif 0 < calculateDistance(layout[line[i]], layout[line[i+1]])/keyWidth <= m.sqrt(2):                          # neighborhood_key
                    total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]]))
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, line[i], line[i+1], total_weight)
                else:
                    total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth # normal_case
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, line[i], line[i+1], total_weight)
                
            # different_layer    
            else:
                if layout[line[i]][1] == layout[line[i+1]][1]:
                    if layout[line[i]][0] == layout[line[i+1]][0]:                                                         # same_x_y_cord
                        total_weight = click_depth + change_layer
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, line[i], line[i+1], total_weight)
                            
                    else:                                                                                                  # different_x_y_cord
                        total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth + change_layer 
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, line[i] , line[i+1], total_weight)       
                else:                                                                                                  # different_x_y_cord
                    total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth + change_layer 
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, line[i] , line[i+1], total_weight)                  

            total += count

        start_char = line[-1]
        line = fp.readline()

    fp.close()


    
    return dict


# In[ ]:


def FittsLaw(W,D):
    #implement the Fitt's Law based on the given arguments and constant
    b = 0.105
    
    mt = b*(m.log2(D/W + 1))
    return mt


# In[ ]:

"""
def FastType(W,D):
    b = 0.127
    mt = b*(m.log2(D/W +1))
    return mt
"""

# In[ ]:


def calculateDistance(a,b):
    x1,y1 = cord[a[0]][a[1]]
    x2,y2 = cord[b[0]][b[1]]
    return m.sqrt(pow((y2-y1),2) + pow((x2 - x1),2))

def compute_weight(tbl):
    without_weight = 0 
    for k, v in tbl.items():
        without_weight += v[3]    
    return without_weight   

def compute_WPM(data_path, without_weight):
    fp = open(data_path)
    line = fp.readline()
    total_char  = 0
    line = line.strip()  
    while line:
        for i in range(len(line)):
            total_char += 1
        line = fp.readline()
    fp.close()
  
    WPM = (total_char/5)/(without_weight/60)
    #WPM = (1 / typing_weight) * (60/5)
    return total_char, WPM   

data_path = 'snu_typing.txt'
print(data_path)

main_dict = makeDigramTable(data_path, layout)

print(main_dict)

without_weight = compute_weight(main_dict)
print(without_weight)

total_char, WPM = compute_WPM(data_path, without_weight)
print("total_char =", total_char)
print("WPM=", WPM)

