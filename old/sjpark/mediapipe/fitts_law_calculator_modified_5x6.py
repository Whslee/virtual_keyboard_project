import os, sys
import math as m
import random
import string
import pandas as pd


# key width equal to 1key
keyWidth = 1.0
# ABC keyboard layout
layout = {'k': (0, 0, 0), 'g': (1, 0, 0), 'd': (2, 0, 0), 'v': (3, 0, 0), 'f': (0, 1, 0), 'n': (1, 1, 0), 'i': (2, 1, 0), 'h': (3, 1, 0),  'w': (4, 1, 0), 'z': (5, 1, 0), 'm': (0, 2, 0), 'o': (1, 2, 0), 'e': (2, 2, 0), 't': (3, 2, 0), 'c': (4, 2, 0), 'x': (5, 2, 0), 'p': (0, 3, 0), 'r': (1, 3, 0), 'a':(2, 3, 0), 's': (3, 3, 0), 'u': (4, 3, 0), 'j': (5, 3, 0), 'l': (2, 4, 0), 'y': (3, 4, 0), 'b': (4, 4, 0), 'q' : (5, 4, 0)}
#key coordinate for a 3 rows by 3 column keyboard
cord = [[(x + keyWidth/2.0, y + keyWidth/2.0) for x in range(6)] for y in range(6)]


def FittsLaw(W,D):
    #implement the Fitt's Law based on the given arguments and constant
    b = 0.105
    
    mt = b*(m.log2(D/W + 1))
    return mt



def calculateDistance(a,b):
    x1,y1 = cord[a[0]][a[1]]
    x2,y2 = cord[b[0]][b[1]]
    return m.sqrt(pow((y2-y1),2) + pow((x2 - x1),2))

def makeDigramTable(data_path, layout):
    fp = open(data_path)
    line = fp.readline()
    total = 0 
    count = 1
    dict = {}
    start_char = 0
    mem_con = 0 
    vowel = ('e', 'a', 'i', 'o', 'u')   

    typing_weight = 0
    click_depth = 0.488
    change_layer = 0.37
    repeat = 1.8

    while line:

        line = line.strip()
        line = line.lower()
        if start_char != 0:
            pair = start_char + ',' + line[0]
            if line[0] not in vowel:                                                                          # consonant
                if start_char not in vowel:                                                                   # consonant-to-consonant
                    # same_layer
                    if layout[start_char][2] == layout[line[0]][2]:
                        if calculateDistance(layout[start_char], layout[line[0]]) == 0:                                             # same_key
                            total_weight = repeat + click_depth
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3] + total_weight)
                            else:
                                dict[pair] = (count, start_char, line[0], total_weight)
                        elif 0< calculateDistance(layout[start_char], layout[line[0]])/keyWidth <= m.sqrt(2):                          # neighborhood_key
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
                
                    # different layer    
                    else:
                        if layout[start_char][1] == layout[line[0]][1]:
                            if layout[start_char][0] == layout[line[0]][0]:                                                         # same_x_y_cord
                                total_weight = click_depth + change_layer
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, start_char, line[0], total_weight)
                            
                            else:                                                                                                   # different_x_cord
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth + change_layer 
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, start_char , line[0], total_weight)  
                        else:
                            if layout[start_char][0] == layout[line[0]][0]:                                                         # different_y_cord
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth + change_layer
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, start_char, line[0], total_weight)
                            
                            else:                                                                                                   # different_x_y_cord
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth + change_layer 
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, start_char , line[0], total_weight)       

                else:                                                                                                              # vowel-to-consonant
                    if mem_con == 0:
                        total_weight = FittsLaw(keyWidth, keyWidth*m.sprt(2)) + change_layer + click_depth
                    else: 
                        total_weight = FittsLaw(keyWidth, calculateDistance(layout[mem_con], layout[line[0]])) + change_layer
                        if pair in dict:
                             dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                        else:
                             dict[pair] = (count, start_char , line[0], total_weight)              
            else:                                                                                                                     # vowel
                if start_char in vowel:                                                                                               # vowel-to-vowel (same)
                    if start_char == line[0]:
                        total_weight = repeat
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, start_char , line[0], total_weight)
                    else:                                                                                                          # vowel-to-vowel (different)
                        total_weight = change_layer
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, start_char , line[0], total_weight)
                else:                                                                                                              # consonant-to-vowel
                    total_weight = change_layer 
                    mem_con = start_char
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, start_char , line[0], total_weight) 
            total += count
            start_char = 0

        for i in range(len(line) -1):
            pair = line[i] + ',' + line[i+1]
            if line[i+1] not in vowel:                                                                                             # consonant
                if line[i] not in vowel:                                                                                           # consonant-to-consonant
                    # same_layer
                    if layout[line[i]][2] == layout[line[i+1]][2]:                                                             
                        if calculateDistance(layout[line[i]], layout[line[i+1]]) == 0:                                             # same_key
                            total_weight = repeat
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, line[i], line[i+1], total_weight)
                        elif 0 <calculateDistance(layout[line[i]], layout[line[i+1]])/keyWidth <= m.sqrt(2):                          # neighborhood_key
                            total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]]))
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, line[i], line[i+1], total_weight)
                        else:
                            total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth    # normal_case
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, line[i], line[i+1], total_weight)
                
                    # different layer    
                    else:
                        if layout[line[i]][1] == layout[line[i+1]][1]:
                            if layout[line[i]][0] == layout[line[i+1]][0]:                                                         # same_x_y_cord
                                total_weight = click_depth + change_layer
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, line[i], line[i+1], total_weight)
                            
                            else:                                                                                                   # different_x_cord
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth + change_layer 
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, line[i] , line[i+1], total_weight)       
                        else:
                            if layout[line[i]][0] == layout[line[i+1]][0]:                                                         # different_y_cord
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth + change_layer
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, line[i], line[i+1], total_weight)
                            
                            else:                                                                                                   # different_x_y_cord
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth + change_layer 
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, line[i] , line[i+1], total_weight)    
                         
  
                else:                                                                                                              # vowel-to-consonant
                    if mem_con == 0:
                        total_weight = FittsLaw(1, m.sqrt(2)) + change_layer + click_depth
                    else: 
                        total_weight = FittsLaw(keyWidth, calculateDistance(layout[mem_con], layout[line[i+1]])) + change_layer + click_depth
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, line[i] , line[i+1], total_weight)              
            else:                                                                                                                  # vowel
                if line[i] in vowel:                                                                                               # vowel-to-vowel (same)
                    if line[i] == line[i+1]:
                        total_weight = repeat
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, line[i] , line[i+1], total_weight)
                    else:                                                                                                          # vowel-to-vowel (different)
                        total_weight = change_layer
                        if pair in dict:
                            dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                        else:
                            dict[pair] = (count, line[i] , line[i+1], total_weight)
                else:                                                                                                              # consonant-to-vowel
                    total_weight = change_layer 
                    mem_con = line[i] 
                    if pair in dict:
                        dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                    else:
                        dict[pair] = (count, line[i] , line[i+1], total_weight) 
            
            total += count

        
        start_char = line[-1]

        line = fp.readline()

    fp.close()
    

    return dict

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


"""
# Make a Digram Table , which is a dictionary with key format (letter_i,letter_j) to its Pij
def makeDigramTable(data_path):
    fp = open(data_path)
    line = fp.readline()
    total = 0 
    count = 1
    dict = {}
    start_char = 0

    while line:

        line = line.strip()
        line = line.lower()
        if start_char != 0:
            pair = start_char + ',' + line[0]
            if pair in dict:
                dict[pair] = (dict[pair][0] + count, line[i], line[i+1])

            if pair not in dict:
                dict[pair] = (count, line[i], line[i+1])
            total += count

        for i in range(len(line) -1):
            pair = line[i] + ',' + line[i+1]
            if pair in dict:
                dict[pair] = (dict[pair][0] + count, line, line[i+1])

            if pair not in dict:
                dict[pair] = (count, line[i].lower(), line[i+1].lower())
            
            total += count

        start_char = line[-1]
        line = fp.readline()

    fp.close()

    for k, v in dict.items():
        dict[k] = (v[0], v[1], v[2], v[0] /total)
    
    return dict
"""







"""
def FastType(W,D):
    b = 0.127
    mt = b*(m.log2(D/W +1))
    return mt
"""

       
"""
def compute_weight(layout, tbl):
    for k, v in tbl.values():
        if val[2] != 'e' or 'a' or 'i' or 'o' or 'u':                                             # consonant
            if val[1] != 'e' or 'a' or 'i' or 'o' or 'u':                                         # consonant-to-consonant
                # same layer
                if layout[val[1]][2] == layout[val[2]][2]:
                    if calculateDistance(layout[val[1]], layout[val[2]])/keyWidth == 0: # same_key
                        total_weight = repeat + click_depth
                        typing_weight += total_weight * val[3]
                    elif calculateDistance(layout[val[1]], layout[val[2]])/keyWidth <= m.sqrt(2): # neighborhood_key
                        total_weight = FittsLaw(keyWidth, calculateDistance(layout[val[1]], layout[val[2]]))
                        typing_weight += total_weight * val[3]
                    else:
                        total_weight = FittsLaw(keyWidth, calculateDistance(layout[val[1]], layout[val[2]])) + click_depth
                        typing_weight += total_weight * val[3]
                
                # different layer    
                else:
                    if layout[val[1]][1] == layout[val[2]][1]:
                        if layout[val[1]][0] == layout[val[2]][0]:                                # same_x_y_cord
                            total_weight = click_depth + change_layer
                            typing_weight += total_weight * val[3]

                        else:                                                                     # different_x_y_cord
                            total_weight = FittsLaw(keyWidth, calculateDistance(layout[val[1]], layout[val[2]])) + click_depth + change_layer 
                            typing_weight += total_weight * val[3]
            
            else:                                                                                 # vowel-to-consonant
                total_weight = FittsLaw(keyWidth, calculateDistance(layout[mem_con], layout[val[2]])) + change_layer
        else:                                                                                     # vowel
            if val[1] == 'e' or 'a' or 'i' or 'o' or 'u':                                         # vowel-to-vowel (same)
                if val[1] == val[2]:
                    total_weight = repeat
                    typing_weight += total_weight * val[3]
                else:                                                                             # vowel-to-vowel (different)
                    total_weight = change_layer
                    typing_weight += total_weight * val[3]
            else:                                                                                 # consonant-to-vowel
                total_weight = change_layer 
                typing_weight += total_weight * val[3]

        if val[1] != 'e' or 'a' or 'i' or 'o' or 'u':
            mem_con = val[1]

    return typing_weight
"""  
                

data_path = 'English500_alphabet_file.txt'
print(data_path)

main_dict = makeDigramTable(data_path, layout)

#digraph = pd.DataFrame(main_dict, index = ['count', 'val1', 'val2', 'weight', 'ratio'])
#digraph.to_excel("./digraph_new_new.xlsx")

without_weight = compute_weight(main_dict)
print(without_weight)

total_char, WPM = compute_WPM(data_path, without_weight)
print("total_char =", total_char)
print("WPM=", WPM)