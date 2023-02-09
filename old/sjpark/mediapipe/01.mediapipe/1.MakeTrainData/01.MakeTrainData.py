import cv2
import mediapipe as mp
import numpy as np
import glob, os
from os import getcwd

#image file names in current dir
IMAGE_FILES = []

#OUTPUT PATH
angle_dataset='angle_dataset_label.txt'
f = open(angle_dataset, 'w')
f.close()

path = os.getcwd() 

#TRAIN IMAGE PATH
f = open('train_all.txt', 'r')

IMAGE_FILES = f.read()
IMAGE_FILES = IMAGE_FILES.split()
f.close()

mp_drawing = mp.solutions.drawing_utils
#mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:

  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    result = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    if result.multi_hand_landmarks is not None:
        for res in result.multi_hand_landmarks:
            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]

            # Compute angles between joints
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
            v = v2 - v1 # [20,3]
            # Normalize 
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

             # Get angle using arcos of dot product
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]
    
            angle = np.degrees(angle) # Convert radian to degree

            # Save data in txt file
            f = open(angle_dataset, 'a')
            for line in angle:
                f.write(str(line) + ',')
            alp=file.split('/')
            alp=alp[-1]
            alp=alp.split('_')
            if alp[0] == 'layer1s':
                num = '0' 
            elif alp[0] == 'layer1c':
                num = '1'     
            elif alp[0] == 'layer2s':
                num = '2'         
            elif alp[0] == 'layer2c':
                num = '3'     
            elif alp[0] == 'layer3s':
                num = '4'         
            elif alp[0] == 'layer3c':
                num = '5'
            elif alp[0] == 'index':
                num = '6'
            elif alp[0] == 'letter-a':
                num = '7'
            elif alp[0] == 'letter-e':
                num = '8'
            elif alp[0] == 'letter-i':
                num = '9'
            elif alp[0] == 'letter-o':
                num = '10'
            elif alp[0] == 'letter-u':
                num = '11'
            f.write(num)
            f.write('\n')
            print(file)
            f.close()




  


