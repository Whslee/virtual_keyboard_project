import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
from timeit import default_timer as timer


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
    cv2.rectangle(keyboardImage, (100, 60), (300, 260), (255, 255, 255), 1, 8, 0)
    cv2.rectangle(keyboardImage, (340, 60), (540, 260), (255, 255, 255), 1, 8, 0)
    cv2.line(keyboardImage, (100, 110), (300, 110), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (100, 160), (300, 160), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (100, 210), (300, 210), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (150, 60), (150, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (200, 60), (200, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (250, 60), (250, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (300, 60), (300, 260), (255, 255, 255), 1, 0, 0)
    
    cv2.line(keyboardImage, (340, 110), (540, 110), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (340, 160), (540, 160), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (340, 210), (540, 210), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (390, 60), (390, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (440, 60), (440, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (490, 60), (490, 260), (255, 255, 255), 1, 0, 0)
    cv2.line(keyboardImage, (540, 60), (540, 260), (255, 255, 255), 1, 0, 0)
    
    cv2.putText(keyboardImage, "K    M    H    U        Z    W    G    U", (115, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A         P    F     E    A", (115, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I         Q    Y    T    I", (115, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O         X    V   J    O", (115, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    
    cv2.putText(keyboardImage, "K    M    H    U        Z    W    G    U", (115, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "C    N    E    A         P    F     E    A", (115, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "D    R    T    I         Q    Y    T    I", (115, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(keyboardImage, "B    S    L    O         X    V   J    O", (115, 240), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1, cv2.LINE_AA)
    
    return keyboardImage

# For webcam input:
idx=0
start_time=timer()
cap = cv2.VideoCapture('data/hand_text.mp4')
fps=cap.get(cv2.CAP_PROP_FPS)
frame_size = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(frame_size)
vid=cv2.VideoWriter('result_vid/hand_text.mp4',cv2.VideoWriter_fourcc(*'DIVX'),fps,frame_size)
with mp_hands.Hands(
    model_complexity=1,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      break

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    # cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
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