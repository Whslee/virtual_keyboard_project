import cv2
import mediapipe as mp
import numpy as np
import math
import glob, os
import time
import copy
from os import getcwd
from Keyboard_layout.Optimized_vowel_3by3 import *

# Video input
videoFile = 'test_video/add_click_vga.mp4'
cap = cv2.VideoCapture(videoFile)
#cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
fps = cap.get(cv2.CAP_PROP_FPS)

print("Starting real-time inference...")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('test_add_click.mp4', fourcc, fps, (640,480))

test_result="result.txt"
f = open(test_result, 'w')
f.close()

max_num_hands = 1
gesture = {
    0:'layer1s', 1:'layer1c', 2:'layer2s', 3:'layer2c', 4:'layer3s', 5:'layer3c', 6:'index',
    7:'letter-a', 8:'letter-e', 9:'letter-i', 10:'letter-o', 11: 'letter-u'
}

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Gesture recognition model
file = np.genfromtxt('./1.MakeTrainData/angle_dataset_label.txt', delimiter=',')
Angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create() #K-Nearest Neighbors Algorithms
knn.train(Angle, cv2.ml.ROW_SAMPLE, label) #Train

frameNum = 0
final_str = []
mem_ready = 0
curr_layer = 'layer1s'
pre_layer = 'layer1s'
pre_layer_select = 0
tipClose = 0
pre_tipClose = 0 
curr_click = 12
prev_click = 12 
stay_count = 0
start_time = time.time()


while cap.isOpened():

    ret, frame = cap.read()
    if ret is False:
        break
    # Image pre-processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]

            # Compute angles between joints
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
            v = v2 - v1 # [20,3]
            # Normalize v
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # Get angle using arcos of dot product
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]
    
            angle = np.degrees(angle) # Convert radian to degree

            # Inference gesture
            data = np.array([angle], dtype=np.float32)
            print(data)
            ret, results, neighbours, dist = knn.findNearest(data, 7)
            idx = int(results[0][0])
            print(gesture[idx])

            # Virtual keyboard
            # Layer selection mode
            if (idx == 0) or (idx == 1):
                layer_select = 1          
            elif (idx == 2) or (idx == 3):
                layer_select = 2
            elif (idx == 4) or (idx == 5):
                layer_select = 3 
            elif (idx == 7) or (idx == 8) or (idx == 9) or (idx == 10) or (idx == 11):
                layer_select = 4 
          
            if (idx == 0) or (idx == 2) or (idx == 4): # layer1/2/3s
                print("Ready gesture is detected.")
                tipClose = 0
                curr_layer = gesture[idx] 
                if (curr_layer == pre_layer): 
                    mem_ready += 1
                else: 
                    mem_ready = 1  

            elif (idx == 1) or (idx == 3) or (idx == 5): # layer1/2/3c
                print("Click gesture is detected.")
                mem_ready = 0
                tipClose = 1
                index_finger = (res.landmark[8].x * 640, res.landmark[8].y *480)
                curr_click = Virtualkeyboard_3by3_select(index_finger, tipClose)
                print("index_finger:", index_finger)
                               
            elif (idx == 7) or (idx == 8) or (idx == 9) or (idx == 10) or (idx == 11):
                print("Vowel gesture is detected.")
                tipClose = 2
                curr_click = Virtualkeyboard_vowel_select(idx, tipClose)              

            if (pre_tipClose ==1) and (curr_click == prev_click):
                move_key = 0 
            elif (pre_tipClose ==2) and (curr_click == prev_click):
                move_key = 0
            elif (pre_tipClose ==0) and (curr_click == prev_click):
                move_key = 1
            elif (pre_tipClose ==0) and (curr_click != prev_click):
                move_key = 1
            else:
                move_key = 1
            print("move_key=", move_key)


            if (move_key == 1):
                stay_count = 0
            else:
                stay_count += 1
                           
            if (stay_count == 3) and (tipClose == 1) and (curr_click < 12):
                curr_str = Select_alphabet(curr_click, layer_select)
                final_str.append(curr_str)
            elif (stay_count == 3) and (tipClose == 2) and (curr_click < 12):
                curr_str = Select_alphabet(curr_click, layer_select)
                if (final_str == True):
                    if (curr_str == pre_curr_str) :
                        if (mem_ready >=3): 
                            final_str.append(curr_str)
                            mem_ready = 0
                    else:
                        final_str.append(curr_str)
                else:
                    if (mem_ready >= 3): 
                        final_str.append(curr_str)

            if (move_key == 1) and (tipClose == 1):
                keyboardImage = Click_effect(index_finger, frame)

    pre_layer = curr_layer
    prev_click = curr_click
    pre_tipClose = tipClose

    # Draw the keyboard layer and monitor selected string
    display_str = ''.join(final_str)
    print("Display string:", display_str)
    keyboardImage = Virtualkeyboard_3by3_draw_layer(frame, display_str, layer_select)
    cv2.putText(frame, str(gesture[idx]), (500,450), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2, cv2.LINE_AA)

    # Show detected results
    #cv2.imshow('Object Detection', frame)

    # Save video file
    out.write(frame)

    #if cv2.waitKey(1) & 0xff == ord('e'):
    #    break
        
    frameNum += 1
    print("frameNum:", frameNum)

    out.write(keyboardImage)
    idx+=1
    print(f'processed {idx}th frame')
    # if cv2.waitKey(1) & 0xFF == 27:
    #   break

    #Draw the keyboard layer and monitor selected string




cap.release()
out.release()
cv2.destroyAllWindows()
end_time = time.time()
run_time = end_time - start_time
print("Runtime:", run_time)
print("FPS:", round(frameNum/run_time, 2))
