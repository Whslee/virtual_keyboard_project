# author: dgkim
# based on the algorithm by https://github.com/kairess/Rock-Paper-Scissors-Machine

import cv2
import mediapipe as mp
import numpy as np

mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles

LIST_FILE_NAME='train_dataset.txt'
TARGET_FILE_NAME='train_angles.csv'
show_image=True
save_image=False; i=0

video_ext=('.mp4','.mkv','.avi')
image_ext=('.jpg','.jpeg','.png')

with open(LIST_FILE_NAME,'r') as f:
    file_list=f.readlines()
    file_list=[x.rsplit(maxsplit=1) for x in file_list if not x.startswith('#') and x.strip()!='']

with open(TARGET_FILE_NAME,'w') as result_file:
    for data, label in file_list:
        if data.endswith(video_ext):
            cap=cv2.VideoCapture(data)
            hands=mp_hands.Hands(model_complexity=1,max_num_hands=1)
            if save_image:
                i+=1
                vid=cv2.VideoWriter(f'hands-result-onefinger-{i}.mp4',cv2.VideoWriter_fourcc(*'DIVX'),30,(720,1280))

            while cap.isOpened():
                success, image=cap.read()
                if not success:
                    print(f'{data}: done')
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

                    angle_str=[f'{x:.8f}' for x in angle]
                    angle_str=','.join(angle_str) + ',' + label + '\n'
                    result_file.write(angle_str)

                    if show_image:
                        mp_drawing.draw_landmarks(
                            image,res,mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style()
                        )
                
                if save_image:
                    vid.write(image)

                if show_image:
                    cv2.imshow('image',image)
                    cv2.waitKey(10)

            cap.release()
            if save_image:
                vid.release()
        
        elif data.endswith(image_ext):
            image=cv2.imread(data)
            if image is None:
                print(f'{data}: does not exist')
                break
            image_cvt=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

            hands=mp_hands.Hands(static_image_mode=True,max_num_hands=1,model_complexity=1)

            results=hands.process(image_cvt)

            if results.multi_hand_landmarks is not None:
                res=results.multi_hand_landmarks[0]
                joint=np.zeros((21,3))
                for j,lm in enumerate(res.landmark):
                    joint[j]=[lm.x,lm.y,lm.z]
                
                # Compute angles between joints
                v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:]  # Parent joint
                v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
                v = v2 - v1 # [20,3]
                # Normalize v
                v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

                # Get angle using arcos of dot product
                angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

                angle = np.degrees(angle) # Convert radian to degree

                angle_str=[f'{x:.8f}' for x in angle]
                angle_str=','.join(angle_str) + ',' + label + '\n'
                result_file.write(angle_str)

                if show_image:
                    mp_drawing.draw_landmarks(
                        image,res,mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style()
                    )
            if show_image:
                cv2.imshow('image',image)
                cv2.waitKey(10)

            if save_image:
                i+=1
                cv2.imwrite(f'hands-result-{i}.jpg',image)