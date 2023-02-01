# 일단 구동가능하게 만들어 놓음 이거는 csv 파일 데이터셋 이용해서 손동작 각도 기반 인식
# 해야 할것 동영상으로 나오게 만들어야 되고, 데이터셋 넣어야되고, 키패드 배열 만들어야됨.
import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
from timeit import default_timer as timer
import numpy as np

def Virtualkeyboard_4x4_draw_layer(keyboardImage, display_str):
    # 왼쪽아래 학교표시
    cv2.rectangle(keyboardImage, (65, 1330), (205, 1360), (100, 0, 0), -1, 8, 0)
    cv2.rectangle(keyboardImage, (65, 1330), (205, 1360), (255, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, "SNU, CAPP Lab HJ.", (20, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 255, 0), 1, cv2.LINE_AA) 
    
    #Display string
    cv2.rectangle(keyboardImage, (90, 808), (650, 852), (255, 255, 255), -1, 8, 0)
    cv2.rectangle(keyboardImage, (90, 808), (650, 852), (0, 255, 0), 1, 8, 0)
    cv2.putText(keyboardImage, display_str, (50, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 50, 50), 2, cv2.LINE_AA)
  
    #Keyboard layer
    cv2.rectangle(keyboardImage, (150, 860), (350, 1060), (255, 255, 255), 1, 8, 0)
    cv2.rectangle(keyboardImage, (390, 860), (590, 1060), (255, 255, 255), 1, 8, 0)
    cv2.line(keyboardImage, (150, 910), (350, 910), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (150, 960), (350, 960), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (150, 1010), (350, 1010), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (200, 860), (200, 1060), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (250, 860), (250, 1060), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (300, 860), (300, 1060), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (350, 860), (350, 1060), (255, 255, 255), 1, 0, 0)
    
    cv2.line(keyboardImage, (390, 910), (590, 910), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (390, 960), (590, 960), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (390, 1010), (590, 1010), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (440, 860), (440, 1060), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (490, 860), (490, 1060), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (540, 860), (540, 1060), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (590, 860), (590, 1060), (255, 255, 255), 1, 0, 0)
    
    cv2.putText(keyboardImage, "K    M    H    U         Z    W    G    U", (165, 890), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A         P    F    E    A", (165, 940), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I         Q    Y    T    I", (165, 990), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O         X    V    J    O", (165, 1040), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    
    cv2.putText(keyboardImage, "K    M    H    U         Z    W    G    U", (165, 890), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A         P    F    E    A", (165, 940), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I         Q    Y    T    I", (165, 990), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O         X    V    J    O", (165, 1040), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    
    return keyboardImage
  

# For webcam input:
idx=0
videofile='data_hyunjun/hand_long_home.mp4'
videosave='result_hyunjun/hand_long_home.mp4'
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
start_time=timer()

cap = cv2.VideoCapture(videofile) # 비디오 연결할때는 0,1,2여러개라면 지정해주어야 함.

fps=cap.get(cv2.CAP_PROP_FPS)
frame_size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frame_size)
vid=cv2.VideoWriter(videosave,cv2.VideoWriter_fourcc(*'DIVX'),fps,frame_size)

max_num_hands = 1
gesture = {
    0:'fist', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five',
    6:'six', 7:'rock', 8:'spiderman', 9:'yeah', 10:'ok',
}

# mediapipe hands model
with mp_hands.Hands(                         # 손가락 detection 모듈 초기화
    model_complexity=1,
    max_num_hands=max_num_hands,                         # 최대 몇개의 손 인식
    min_detection_confidence=0.5,            # 0.5가 가장 좋다고 함.
    min_tracking_confidence=0.5) as hands:

# Gesture recognition model
  file = np.genfromtxt('data_hyunjun/gesture_train.csv',delimiter=',') # 데이터 파일 경로 입력
  angle = file[:,:-1].astype(np.float32)
  label = file[:, -1].astype(np.float32)
  knn = cv2.ml.KNearest_create()             # K-Nearest Neighbors 알고리즘
  knn.train(angle, cv2.ml.ROW_SAMPLE,label)



  while cap.isOpened():                      # 카메라가 열려있으면 1프레임씩 읽어오는 것.
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      break


    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(cv2.flip(image,-1), cv2.COLOR_BGR2RGB)       # mediapipe는 RGB, OpenCV는 BGR 이라 바꿔주어야함.
    results = hands.process(image)                                    # 앞에 전처리 부분 , cv2.flip(image,0)0은 상하반전,1은 좌우반전 을 추가해서 다시 뒤집어줌
                                                                      # -1은 상하 좌우반전
    # Draw the hand annotations on the image.
    image.flags.writeable = True                                      # 손인식이 되면 True가 됨
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)                    # 이미지를 출력해야하니 다시 RGB,BGR 바꿔줌
    if results.multi_hand_landmarks is not None:
      for res in results.multi_hand_landmarks:
          joint = np.zeros((21,3))
          for j , lm in enumerate(res.landmark):
              joint[j] = [lm.x, lm.y, lm.z]

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


          # Inference gesture
          data = np.array([angle], dtype=np.float32)
          print(data)
          ret, results, neighbours, dist = knn.findNearest(data, 11)
          idx = int(results[0][0])
          print(gesture[idx])

          # keyboard gesture
          cv2.putText(image, text=gesture[idx].upper(), org=(int(res.landmark[0].x* image.shape[1]),
          int(res.landmark[0].y *image.shape[0]+20)), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
          fontScale=1, color=(255,255,255), thickness=2 )


          mp_drawing.draw_landmarks(
            image,res,mp_hands.HAND_CONNECTIONS,
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

    #Draw the keyboard layer and monitor selected string

cap.release()
vid.release()
fps=idx/(timer()-start_time)
print(f'fps: {fps}')