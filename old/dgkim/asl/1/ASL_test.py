import cv2
import mediapipe as mp
import numpy as np

max_num_hands = 2
numbers = {
    'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6,
    'seven' : 7, 'eight' : 8, 'nine' : 9, 'ten' : 10
}

# Mediapipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

# numbers recognition model
file = np.genfromtxt('sign_train.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

# Video file input
cap = cv2.VideoCapture("ASL_numbers_sample.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)

# Define the codec and create VideoWriter Object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter()
success = out.open('ASL_sample_result.mp4',fourcc, 15.0, (640,480),True)

idx_list = []

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        success, img = cap.read()
        if not success:
            # If loading a video, use 'break' instead of 'continue'.
            print("Ignoring empty camera frame.")
            break
        
        img = cv2.flip(img, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        result = hands.process(img)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

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

                # Inference numbers
                data = np.array([angle], dtype=np.float32)
                ret, results, neighbours, dist = knn.findNearest(data, 3)
                idx = int(results[0][0])
                idx_list.append(idx)
                
        img.flags.writeable = False
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img)

        img.flags.writeable = True
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            img_height, img_width, _ = img.shape
            for hand_landmarks in results.multi_hand_landmarks:
                print('hand_landmakrs:', hand_landmarks)
                print(f'Index finger tip coordinates: (',
                        f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * img_width},'
                        f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * img_height})'
                )

            # Draw the hand annotation on the img
            mp_drawing.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
            
            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            keys = list(numbers.keys())
        
            if idx in numbers.values():
                cv2.putText(
                    img, 
                    text = keys[idx - 1],
                    org=(int(res.landmark[0].x * img.shape[1]),
                        int(res.landmark[0].y * img.shape[0] + 20)), 
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, 
                    color=(255, 255, 255), 
                    thickness=2)
            
            cv2.flip(img, 1)
            out.write(img)

            if cv2.waitKey(1) & 0xFF == ord('e'):
                break

# Close all the opened frames            
cap.release()
cv2.destroyAllWindows()

def slice_consecutive_duplicates(lst, n):
    sublists = []
    current = lst[0]
    count = 1
    for i in lst[1:]:
        if current == i:
            count += 1
        else:
            if count >= n:
                sublists.append(current)
            current = i
            count = 1
    if count >= n:
        sublists.append(current)
    return sublists

idx_list = slice_consecutive_duplicates(idx_list, 10)

output_list = []

for numbers in idx_list:
   output_list.append("detected ASL number: " + str(numbers))
    

np.savetxt('ASL_sample_result.txt', output_list, fmt = '%s', delimiter=',')
                

