# author: dgkim
# based on the algorithm by https://github.com/kairess/Rock-Paper-Scissors-Machine

import cv2
import mediapipe as mp
import numpy as np

TRAIN_DATASET_PATH='train_angles_onefinger.csv'
TEST_DATASET_PATH='hands-21.mp4'
RESULT_VIDEO_PATH='test-onefinger2.mp4'

gesture=['None','1-click','2-click']

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

data=np.genfromtxt(TRAIN_DATASET_PATH,delimiter=',')
angle=data[:,:-1].astype(np.float32)
label=data[:,-1].astype(np.float32)
knn=cv2.ml.KNearest_create()
knn.train(angle,cv2.ml.ROW_SAMPLE,label)

cap = cv2.VideoCapture(TEST_DATASET_PATH)
vid=cv2.VideoWriter(RESULT_VIDEO_PATH,cv2.VideoWriter_fourcc(*'DIVX'),30,(720,1280))


hands=mp_hands.Hands(model_complexity=1,max_num_hands=1)
while cap.isOpened():
    success, image=cap.read()
    if not success:
        print('done')
        break
    image_cvt=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    results=hands.process(image_cvt)
    if results.multi_hand_landmarks is not None:
        res=results.multi_hand_landmarks[0]
        joint=np.zeros((21,3))
        for j,lm in enumerate(res.landmark):
            joint[j]=[lm.x,lm.y,lm.z]

        # Compute angles between joints
        v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:]  # Parent joint
        v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
        v = v2 - v1
        # Normalize v
        v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

        # Get angle using arcos of dot product
        angle = np.arccos(np.einsum('nt,nt->n',
        v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
        v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

        angle = np.degrees(angle) # Convert radian to degree

        data=np.array([angle],dtype=np.float32)
        ret,results,neighbors,dist=knn.findNearest(data,11)
        idx=int(results[0][0])
        print(idx)

        cv2.putText(image,text=gesture[idx],org=(0,100),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(0,255,0),thickness=2)

    vid.write(image)
    cv2.imshow('image',image)
    cv2.waitKey(1)

cap.release()
vid.release()