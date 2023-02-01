import cv2
import mediapipe as mp
import numpy as np
import time, os


gesture = {
    0 : '1click', 1 : '2click', 3 :'vclick'
}

# MediaPipe hands model
mp_hands = mp.solutions.hands             # 핸드모델 이니셜 라이즈
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

f = open('test.txt','w') 
#os.makedirs('data_hyunjun', exist_ok=True) # 데이터 셋 저장할 폴더
file = np.genfromtxt('data_hyunjun', delimiter = ',')
angleFile = file[:,:-1]
labelFile = file[:,-1]
angle = angleFile.astype(np.float32)
label = labelFile.astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle,cv2.ml.ROW_SAMPLE,label)
cap = cv2.VideoCapture(0)          # 웹캠

startTime = time.time()
prev_index = 0
sentence = ''
recognizeDelay = 1

while True:
        ret, img = cap.read()
        if not ret:
            continue
        imgRGB = cv2.cvtColor(ing,cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)

        if result.multi_hand_landmarks is not None:
            for res in result.multi_hand_landmarks:
                joint = np.zeros((21,3))
                for j, lm in enumerate(res.landmark):
                        joint[j] = [lm.x, lm.y, lm.z]  

                # Compute angles between joints           각도 구하는 코드들
                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                
                v = v2 - v1 # [20, 3]
                # Normalize v
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]
                compareV1 = v[[0,1,2,4,5,6,7,8,9,10,12,13,14,16,17],:]
                compareV2 = v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:]
                angle = np.arccos(np.einsum('nt,nt->n',compareV1,compareV2))

                angle = np.degrees(angle) # Convert radian to degree
                if keyboard.is_pressed('a'):
                    for num in angle:
                        num = round(num,6)
                        f.write(str(num))
                        f.write(',')
                    f.write("0.00000")  # 데이터를 저장할 gesture의 label번호
                    f.write('\n')
                    print("next")
                data = np.array([angle],dtype=np.float32)
                ret,results,neighbors,dist = knn.findNearest(data,3)
                index = int(results[0][0])
                if index in gesture.keys():
                    if index != prev_index:
                        startTime = time.time()
                        prev_index = index
                    else:
                        if time.time() - startTime > recognizeDelay:
                            if index == 2:
                                sentence += ' '
                            elif index == 3:
                                sentence = ''
                            else:
                                sentence += gesture[index]
                            startTime = time.time()

                    cv2.putText(img,gesture[index].upper(),(int(res.landmark[0].x * img.shape[1] - 10),
                                int(res.landmark[0].y * img.shape[0] + 40)),cv2.FONT_HERSHEY_SIMPLEX, 1, color=(255,255,255))

                mp_drawing.draw_landmarks(img,res,mp_hands.HAND_CONNECTIONS)
        cv2.putText(img,sentence,(20,440),cv2.FONT_HERSHEY_SIMPLEX,2,(255,255,255),3)

        cv2.imshow('HandTracking',img)
        cv2.waitKey(1)
        if keyboard.is_pressed('b'):
             break
f.close();







