

import cv2
import time

def Click_effect(fingertip, keyboardImage):

    #PlaySound(TEXT("WavFiles/mouseclick.wav"), NULL, SND_ASYNC)
    #winsound.PlaySound('WavFiles/mouseclick.wav', winsound.SND_FILENAME)
    
    if(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 60) and (fingertip[1] < 110):
        cv2.rectangle(keyboardImage, (200, 60), (280, 110), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 60) and (fingertip[1] < 110):
        cv2.rectangle(keyboardImage, (280, 60), (360, 110), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 60) and (fingertip[1] < 110):
        cv2.rectangle(keyboardImage, (360, 60), (440, 110), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 110) and (fingertip[1] < 160):
        cv2.rectangle(keyboardImage, (200, 110), (280, 160), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 110) and (fingertip[1] < 160):
        cv2.rectangle(keyboardImage, (280, 110), (360, 160), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 110) and (fingertip[1] < 160):
        cv2.rectangle(keyboardImage, (360, 110), (440, 160), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 160) and (fingertip[1] < 210):
        cv2.rectangle(keyboardImage, (200, 160), (280, 210), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 160) and (fingertip[1] < 210):
        cv2.rectangle(keyboardImage, (280, 160), (360, 210), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 160) and (fingertip[1] < 210):
        cv2.rectangle(keyboardImage, (360, 160), (440, 210), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 200) and (fingertip[0] < 280) and (fingertip[1] >= 210) and (fingertip[1] < 260):
        cv2.rectangle(keyboardImage, (200, 210), (280, 260), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 280) and (fingertip[0] < 360) and (fingertip[1] >= 210) and (fingertip[1] < 260):
        cv2.rectangle(keyboardImage, (280, 210), (360, 260), (255, 255, 255), -1, 8, 0)
    elif(fingertip[0] >= 360) and (fingertip[0] < 440) and (fingertip[1] >= 210) and (fingertip[1] < 260):
        cv2.rectangle(keyboardImage, (360, 210), (440, 260), (255, 255, 255), -1, 8, 0)
    else:
        curr_click = 12
    
    return keyboardImage

def Select_alphabet(curr_click, layer_select):

    key_str_layer1 = ['K', 'M', 'H', 'U', 'C', 'N', 'E', 'A', 'D', 'R', 'T', 'I', 'B', 'S', 'L', 'O']
    key_str_layer2 = ['Z', 'W', 'G', 'U', 'P', 'F', 'E', 'A', 'Q', 'Y', 'T', 'I', 'X', 'V', 'J', 'O']
    #key_str_layer4 = ['A', 'E', 'I', 'O', 'U']
    
    if (layer_select == 1):
        curr_str = key_str_layer1[curr_click]
    elif (layer_select == 2):
        curr_str = key_str_layer2[curr_click]
    elif (layer_select == 4):
        curr_str = key_str_layer4[curr_click]
    
    return curr_str

def Virtualkeyboard_3by3_select(fingertip, tipClose):
    # This function is for setecting the Key from the keyboard layout
    
    dell_click = 0      # Click Detect Key
    reset_click = 0     # Click Reset Key
    curr_click = 12     # Current Key set to None (12 is None)
    
    # If (right_clickSignal == 1)
    if(tipClose == 1):
        if(fingertip[0] >= 160) and (fingertip[0] < 240) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 0
        elif(fingertip[0] >= 240) and (fingertip[0] < 320) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 1
        elif(fingertip[0] >= 320) and (fingertip[0] < 400) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 2
        elif(fingertip[0] >= 400) and (fingertip[0] < 480) and (fingertip[1] >= 60) and (fingertip[1] < 110):
            curr_click = 3
        elif(fingertip[0] >= 160) and (fingertip[0] < 240) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 4
        elif(fingertip[0] >= 240) and (fingertip[0] < 320) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 5
        elif(fingertip[0] >= 320) and (fingertip[0] < 400) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 6
        elif(fingertip[0] >= 400) and (fingertip[0] < 480) and (fingertip[1] >= 110) and (fingertip[1] < 160):
            curr_click = 7
        elif(fingertip[0] >= 160) and (fingertip[0] < 240) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 8
        elif(fingertip[0] >= 240) and (fingertip[0] < 320) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 9 
        elif(fingertip[0] >= 320) and (fingertip[0] < 400) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 10 
        elif(fingertip[0] >= 400) and (fingertip[0] < 480) and (fingertip[1] >= 160) and (fingertip[1] < 210):
            curr_click = 11
        elif(fingertip[0] >= 160) and (fingertip[0] < 240) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            curr_click = 12
        elif(fingertip[0] >= 240) and (fingertip[0] < 320) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            curr_click = 13
        elif(fingertip[0] >= 320) and (fingertip[0] < 400) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            curr_click = 14
        elif(fingertip[0] >= 400) and (fingertip[0] < 480) and (fingertip[1] >= 210) and (fingertip[1] < 260):
            curr_click = 15
        else:
            curr_click = 16
    
    return curr_click, reset_click, dell_click

def Virtualkeyboard_vowel_select(layer, tipClose):
    # This function is for setecting the Vowel. 

    dell_click = 0      # Click Detect Key
    reset_click = 0     # Click Reset Key
    curr_click = 12     # why 12??? only 5 elements in key_str_layer4 ['A', 'E', 'I', 'O', 'U']

    if(tipClose == 2):
        if layer == 'letter-a':
            curr_click = 0
        elif layer == 'letter-e':
            curr_click = 1
        elif layer == 'letter-i':
            curr_click = 2
        elif layer == 'letter-o':
            curr_click = 3
        elif layer == 'letter-u':
            curr_click = 4
        else:
            curr_click = 12     ### ???
    return curr_click, reset_click, dell_click

def Virtualkeyboard_4x4_draw_layer(keyboardImage, display_str):
    
    # 왼쪽아래 학교표시
    cv2.rectangle(keyboardImage, (15, 430), (155, 460), (100, 0, 0), -1, 8, 0)
    cv2.rectangle(keyboardImage, (15, 430), (155, 460), (255, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, "SNU, CAPP Lab.", (20, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 255, 0), 1, cv2.LINE_AA)
     
    #Display string
    cv2.rectangle(keyboardImage, (40, 8), (600, 52), (255, 255, 255), -1, 8, 0)
    cv2.rectangle(keyboardImage, (40, 8), (600, 52), (0, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, display_str, (50, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 50, 50), 2, cv2.LINE_AA)
    
    #Keyboard layer
    cv2.rectangle(keyboardImage, (160, 480), (60, 260), (255, 255, 255), 1, 8, 0)
    cv2.line(keyboardImage, (160, 110), (480, 110), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (160, 160), (480, 160), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (160, 210), (480, 210), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (240, 60), (240, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (320, 60), (320, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (440, 60), (440, 260), (255, 255, 255), 1, 0, 0)
    
    if (layer_select == 1):
        cv2.putText(keyboardImage, "K    M    H    U" (171, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "K    M    H    U" (171, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "C    N    E    A" (171, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "C    N    E    A" (171, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "D    R    T    I" (171, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "D    R    T    I" (171, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "B    S    L    O" (171, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "B    S    L    O" (171, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z    W    G    U" (191, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "P    F    E    A" (191, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q    Y    T    I" (191, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "X    V    J    O" (191, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    if (layer_select == 2):
        cv2.putText(keyboardImage, "Z    W    G    U" (191, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Z    W    G    U" (191, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "P    F    E    A" (191, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "P    F    E    A" (191, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q    Y    T    I" (191, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "Q    Y    T    I" (191, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "X    V    J    O" (191, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "X    V    J    O" (191, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
        cv2.putText(keyboardImage, "K    M    H    U" (171, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "C    N    E    A" (171, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "D    R    T    I" (171, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(keyboardImage, "B    S    L    O" (171, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    return keyboardImage
  