import cv2
import mediapipe as mp
import numpy as np
import os
from os import listdir

max_num_hands = 2
numbers = {
    'one' : 1, 'two' : 2, 'thr' : 3, 'fou' : 4, 'fiv' : 5, 'six' : 6,
    'sev' : 7, 'eig' : 8, 'nin' : 9, 'ten' : 10
}

#mediapipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


#create csv file
file = np.genfromtxt('sign_train.csv', delimiter = ',')
print(file.shape)

# Sign recognition data
IMAGE_FILES = []
FOLDER_LIST =[]
for folders in os.listdir("/Users/mirpark/Desktop/ASL_Numbers/data"):
    folder_dir = os.listdir("/Users/mirpark/Desktop/ASL_Numbers/data/" + folders)
    FOLDER_LIST.extend(folder_dir)
    for images in folder_dir:
        img = cv2.imread(("/Users/mirpark/Desktop/ASL_Numbers/data/" + folders + "/" + images))
        IMAGE_FILES.append(img)
               
#print(FOLDER_LIST)

with mp_hands.Hands(
            static_image_mode = True,
            max_num_hands = max_num_hands,
            min_detection_confidence = 0.5) as hands:
    
    for idx, file_num in enumerate(IMAGE_FILES):
        image = cv2.flip(file_num, 1)
        result = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        images = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        
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
                
                data = np.array([angle], dtype=np.float32)
                label = numbers[FOLDER_LIST[idx][0:3]]
                data = np.append(data, label)
                file = np.vstack((file, data))
                print(file)
                print(file.shape)
                
                mp_drawing.draw_landmarks(image, res, mp_hands.HAND_CONNECTIONS)
                
np.savetxt('sign_train_fy.csv', file, delimiter=',')
                
                
       