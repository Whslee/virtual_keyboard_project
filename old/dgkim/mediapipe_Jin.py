# 요고는 간단하게 손거리 이용해서 어떤것이 가까운지 판별

import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
from timeit import default_timer as timer
import numpy as np


def Virtualkeyboard_4x4_draw_layer(keyboardImage, display_str):
    
    # 왼쪽아래 학교표시
    #cv2.rectangle(keyboardImage, (15, 430), (155, 460), (100, 0, 0), -1, 8, 0)
    #cv2.rectangle(keyboardImage, (15, 430), (155, 460), (255, 255, 0), 1, 8, 0)
    #cv2.putText(keyboardImage, "SNU, CAPP Lab.", (20, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 255, 0), 1, cv2.LINE_AA)
     
    #Display string
    #cv2.rectangle(keyboardImage, (40, 8), (600, 52), (255, 255, 255), -1, 8, 0)
    #cv2.rectangle(keyboardImage, (40, 8), (600, 52), (0, 255, 0), 1, 8, 0)
    #cv2.putText(keyboardImage, display_str, (50, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 50, 50), 2, cv2.LINE_AA)
    
    #Keyboard layer
    cv2.rectangle(keyboardImage, (160, 480), (60, 260), (255, 255, 255), 1, 8, 0)
    cv2.line(keyboardImage, (160, 110), (480, 110), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (160, 160), (480, 160), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (160, 210), (480, 210), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (240, 60), (240, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (320, 60), (320, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (440, 60), (440, 260), (255, 255, 255), 1, 0, 0)

    cv2.putText(keyboardImage, "K    M    H    U" ,(171, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "K    M    H    U" ,(171, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A" ,(171, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A" ,(171, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I" ,(171, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I" ,(171, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O" ,(171, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O" ,(171, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "Z    W    G    U" ,(191, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "P    F    E    A" ,(191, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "Q    Y    T    I" ,(191, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "X    V    J    O" ,(191, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.putText(keyboardImage, "Z    W    G    U" ,(191, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "Z    W    G    U" ,(191, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "P    F    E    A" ,(191, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "P    F    E    A" ,(191, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "Q    Y    T    I" ,(191, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "Q    Y    T    I" ,(191, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "X    V    J    O" ,(191, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "X    V    J    O" ,(191, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 153, 255), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "K    M    H    U" ,(171, 89),  cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A" ,(171, 139), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I" ,(171, 189), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O" ,(171, 239), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)

    return keyboardImage
 

# For webcam input:2
idx=0
videofile='data_hyunjun/hand_test_2.mp4'
videosave='result_hyunjun/hand_test_2.mp4'
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
start_time=timer()

cap = cv2.VideoCapture(videofile) # 비디오 연결할때는 0,1,2여러개라면 지정해주어야 함.

fps=cap.get(cv2.CAP_PROP_FPS)
frame_size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frame_size)
vid=cv2.VideoWriter(videosave,cv2.VideoWriter_fourcc(*'DIVX'),fps,frame_size)
with mp_hands.Hands(                         # 손가락 detection 모듈 초기화
    model_complexity=1,
    max_num_hands=1,                         # 최대 몇개의 손 인식
    min_detection_confidence=0.5,            # 0.5가 가장 좋다고 함.
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():                      # 카메라가 열려있으면 1프레임씩 읽어오는 것.
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      break


    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(cv2.flip(image,-1), cv2.COLOR_BGR2RGB)        # mediapipe는 RGB, OpenCV는 BGR 이라 바꿔주어야함.
    results = hands.process(image)                                    # 앞에 전처리 부분 , cv2.flip(image,0)0은 상하반전,1은 좌우반전 을 추가해서 다시 뒤집어줌
                                                                      # -1은 상하 좌우반전
    # Draw the hand annotations on the image.
    image.flags.writeable = True                                      # 손인식이 되면 True가 됨
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)                    # 이미지를 출력해야하니 다시 RGB,BGR 바꿔줌
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        
          thumb = hand_landmarks.landmark[4]
          index = hand_landmarks.landmark[8]
          middle = hand_landmarks.landmark[12]

          diff_I = abs(index.y - thumb.y)
          diff_M = abs(middle.y - thumb.y)

          distance_I = int(diff_I * 500)
          distance_M = int(diff_M * 500)

          cv2.putText(
            image, text = 'distance_I: %d , distance_M: %d' %(distance_I , distance_M), org=(10,30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1,
            color=255, thickness=2
            )

          mp_drawing.draw_landmarks(
            image,hand_landmarks,mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
          
    # Flip the image horizontally for a selfie-view display.

    #cv2.imshow('image',image)
    #if cv2.waitKey(1) == ord('q'):
    #    break

    #cv2.imwrite('result2/img{:0>3}.png'.format(idx),image)
    display_str = 'hi'
    image = Virtualkeyboard_4x4_draw_layer(image, display_str)
    vid.write(image)
    idx+=1
    print(f'processed {idx}th frame')
    # if cv2.waitKey(1) & 0xFF == 27:
    #   break
    
    # Draw the keyboard layer and monitor selected string
    #display_str = ''.join(final_str)
    #print("Display string:", display_str)
    #keyboardImage = Virtualkeyboard_3by3_draw_layer(frame, display_str, layer_select)
    #cv2.putText(frame, str(gesture[idx]), (500,450), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2, cv2.LINE_AA)


    #Draw the keyboard layer and monitor selected string

cap.release()
vid.release()
fps=idx/(timer()-start_time)
print(f'fps: {fps}')