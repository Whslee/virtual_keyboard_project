import os, sys
import math as m
import random
import string

# key width equal to 1key
keyWidth = 1.0
# layout_awared keyboard layout
layout = {'f': (0, 0, 0), 'm': (1, 0, 0), 'r': (2, 0, 0), 'n': (0, 1, 0), 't': (1, 1, 0), 'd': (2, 1, 0), 'g': (0, 2, 0), 's': (1, 2, 0),  'h': (2, 2, 0), 'j': (0, 0, 1), 'b': (1, 0, 1), 'p': (2, 0, 1), 'q': (0, 1, 1), 'l': (1, 1, 1), 'v': (2, 1, 1), 'z': (0, 2, 1), 'c': (1, 2, 1), 'w': (2, 2, 1), 'o': (0, 0, 2), 'a': (1, 0, 2), 'x': (2, 0, 2), 'u': (0, 1, 2), 'y': (1, 1, 2), 'e': (2, 1, 2), 'i': (0, 2, 2), 'k': (1, 2, 2)}
#key coordinate for a 3 rows by 3 column keyboard
cord = [[(x + keyWidth/2.0, y + keyWidth/2.0) for x in range(3)] for y in range(3)]


def FittsLaw(W,D):
    #implement the Fitt's Law based on the given arguments and constant

    b = 0.105
    
    mt =b*(m.log2(D/W + 1))
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
  
        line = ''.join(filter(str.isalnum, line))
        line = ''.join([i for i in line if not i.isdigit()])
        line = line.replace(" ", "")
        line = line.replace("\n","")
        line = line.strip()
        line = line.lower()

        if len(line) == 0:
            line = fp.readline()
            continue
        else:
            if start_char != 0:
                pair = start_char + ',' + line[0]
                if line[0] not in vowel:                                                                          # consonant
                    if start_char not in vowel:                                                                   # consonant-to-consonant
                        # same_layer
                        if layout[line[0]][2] == layout[start_char][2] :
                            if calculateDistance(layout[start_char], layout[line[0]]) == 0:                                             # same_layer, same_position
                                total_weight = click_depth
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3] + total_weight)
                                else:
                                    dict[pair] = (count, start_char, line[0], total_weight)
                            else:
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth # same_layer, diff_position_key
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, start_char, line[0], total_weight)
                
                        # different_layer    
                        else:                            
                            if calculateDistance(layout[start_char], layout[line[0]]) == 0:                                             # diff_layer, same_position_key
                                total_weight = click_depth + change_layer
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3] + total_weight)
                                else:
                                    dict[pair] = (count, start_char, line[0], total_weight)
                            else:
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[start_char], layout[line[0]])) + click_depth + change_layer # diff_layer, diff_position_key
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, start_char, line[0], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, start_char, line[0], total_weight)
  
                    else:                                                                                                              # vowel-to-consonant
                        if mem_con == 0:
                            total_weight = FittsLaw(keyWidth, keyWidth*m.sqrt(2)) + change_layer + click_depth
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, start_char , line[0], total_weight)  
       
                        else: 
                            total_weight = FittsLaw(keyWidth, calculateDistance(layout[mem_con], layout[line[0]])) + change_layer + click_depth
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, start_char , line[0], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, start_char , line[0], total_weight)    
          
                else:                                                                                                                     # vowel
                    if start_char in vowel:                                                                                               # vowel-to-vowel (same)
                        if start_char == line[0]:
                            total_weight = change_layer * 2
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
                        if layout[line[i+1]][2] == layout[line[i]][2]:
                            if calculateDistance(layout[line[i]], layout[line[i+1]]) == 0:                                             # same_position_key
                                total_weight = click_depth
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3] + total_weight)
                                else:
                                    dict[pair] = (count, line[i], line[i+1], total_weight)
                            else:
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth # different_position_key
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, line[i], line[i+1], total_weight)
                
                        # diff_layer   
                        else:                            
                            if calculateDistance(layout[line[i]], layout[line[i+1]]) == 0:                                             # same_position_key
                                total_weight = click_depth + change_layer
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3] + total_weight)
                                else:
                                    dict[pair] = (count, line[i], line[i+1], total_weight)
                            else:
                                total_weight = FittsLaw(keyWidth, calculateDistance(layout[line[i]], layout[line[i+1]])) + click_depth + change_layer # different_position_key
                                if pair in dict:
                                    dict[pair] = (dict[pair][0] + count, line[i], line[i+1], dict[pair][3]+total_weight)
                                else:
                                    dict[pair] = (count, line[i], line[i+1], total_weight)
                      
                    else:                                                                                                              # vowel-to-consonant
                        if mem_con == 0:
                            total_weight = FittsLaw(keyWidth, keyWidth*m.sqrt(2)) + change_layer + click_depth
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, line[i] , line[i+1], total_weight)     
       
                        else: 
                            total_weight = FittsLaw(keyWidth, calculateDistance(layout[mem_con], layout[line[i+1]])) + change_layer + click_depth
                            if pair in dict:
                                dict[pair] = (dict[pair][0] + count, line[i] , line[i+1], dict[pair][3]+total_weight)
                            else:
                                dict[pair] = (count, line[i] , line[i+1], total_weight)    
            
                else:                                                                                                                  # vowel
                    if line[i] in vowel:                                                                                               # vowel-to-vowel (same)
                        if line[i] == line[i+1]:
                            total_weight = change_layer * 2
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

    while line:
        line = ''.join(filter(str.isalnum, line))
        line = ''.join([i for i in line if not i.isdigit()])
        line = line.replace(" ", "")
        line = line.replace("\n","")
        line = line.strip()
        
        if len(line) == 0:
            line = fp.readline()
            continue
        else:
            for i in range(len(line)):
                total_char += 1
            #print(line, total_char)
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
                

"""
data_path_0 = 'Life_English_original_1,577.txt'
data_path_1 = 'Ebook1_Alice_original_28,384.txt'
data_path_2 = 'Ebook2_20000Leagues_original_101,979.txt'
data_path_3 = 'Ebook3_Gulliver_original_106,015.txt'
data_path_4 = 'Ebook4_LesMiserables_original_568,568.txt'

main_dict_0 = makeDigramTable(data_path_0, layout)
main_dict_1 = makeDigramTable(data_path_1, layout)
main_dict_2 = makeDigramTable(data_path_2, layout)
main_dict_3 = makeDigramTable(data_path_3, layout)
main_dict_4 = makeDigramTable(data_path_4, layout)

without_weight_0 = compute_weight(main_dict_0)
without_weight_1 = compute_weight(main_dict_1)
without_weight_2 = compute_weight(main_dict_2)
without_weight_3 = compute_weight(main_dict_3)
without_weight_4 = compute_weight(main_dict_4)

total_char_0, WPM_0 = compute_WPM(data_path_0, without_weight_0)
total_char_1, WPM_1 = compute_WPM(data_path_1, without_weight_1)
total_char_2, WPM_2 = compute_WPM(data_path_2, without_weight_2)
total_char_3, WPM_3 = compute_WPM(data_path_3, without_weight_3)
total_char_4, WPM_4 = compute_WPM(data_path_4, without_weight_4)

print(data_path_0)
print("Ttot=", without_weight_0)
print("total_char =", total_char_0)
print("WPM=", WPM_0)

print(data_path_1)
print("Ttot=", without_weight_1)
print("total_char =", total_char_1)
print("WPM=", WPM_1)

print(data_path_2)
print("Ttot=", without_weight_2)
print("total_char =", total_char_2)
print("WPM=", WPM_2)

print(data_path_3)
print("Ttot=", without_weight_3)
print("total_char =", total_char_3)
print("WPM=", WPM_3)

print(data_path_4)
print("Ttot=", without_weight_4)
print("total_char =", total_char_4)
print("WPM=", WPM_4)
"""

data_path_0 = 'faith.txt'
data_path_1 = 'love.txt'
data_path_2 = 'peace.txt'
data_path_3 = 'poet.txt'

main_dict_0 = makeDigramTable(data_path_0, layout)
main_dict_1 = makeDigramTable(data_path_1, layout)
main_dict_2 = makeDigramTable(data_path_2, layout)
main_dict_3 = makeDigramTable(data_path_3, layout)


without_weight_0 = compute_weight(main_dict_0)
without_weight_1 = compute_weight(main_dict_1)
without_weight_2 = compute_weight(main_dict_2)
without_weight_3 = compute_weight(main_dict_3)

total_char_0, WPM_0 = compute_WPM(data_path_0, without_weight_0)
total_char_1, WPM_1 = compute_WPM(data_path_1, without_weight_1)
total_char_2, WPM_2 = compute_WPM(data_path_2, without_weight_2)
total_char_3, WPM_3 = compute_WPM(data_path_3, without_weight_3)

print(data_path_0)
print("Ttot=", without_weight_0)
print("total_char =", total_char_0)
print("WPM=", WPM_0)

print(data_path_1)
print("Ttot=", without_weight_1)
print("total_char =", total_char_1)
print("WPM=", WPM_1)

print(data_path_2)
print("Ttot=", without_weight_2)
print("total_char =", total_char_2)
print("WPM=", WPM_2)

print(data_path_3)
print("Ttot=", without_weight_3)
print("total_char =", total_char_3)
print("WPM=", WPM_3)

