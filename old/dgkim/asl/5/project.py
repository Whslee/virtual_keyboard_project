import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
import cv2
import mediapipe as mp 

file=''
device = torch.device("cuda:0")



class MLP4(nn.Module) :
    def __init__(self, input_dim=19) :
        super().__init__()
        self.linear = nn.Linear(input_dim, 38, bias=True)
        self.linear2 = nn.Linear(38, 38, bias=True)
        self.linear3 = nn.Linear(38, 10, bias=True)
        
    def forward(self, x) :
        x = nn.functional.leaky_relu(self.linear(x))
        x = nn.functional.leaky_relu(self.linear2(x))
        x = self.linear3(x)
        return x

model = torch.load("fc.pt", map_location=device)

class MLP4(nn.Module) :
    def __init__(self, input_dim=5) :
        super().__init__()
        self.conv = nn.Conv1d(1,1,3,3)
        self.linear = nn.Linear(input_dim, 15, bias=True)
        self.linear2 = nn.Linear(15, 10, bias=True)
        
    def forward(self, x) :
        x = x.float().view(-1,1,15)
        x=nn.functional.leaky_relu(self.conv(x))
        x=x.view(-1,5)
        x = nn.functional.leaky_relu(self.linear(x))
        x = self.linear2(x)
        return x

model2 = torch.load("1d.pt", map_location=device)

max_num_hands =1

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands = max_num_hands,
    min_detection_confidence = 0.5,
    min_tracking_confidence = 0.5
)

def angles(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result=hands.process(imgRGB)
    
    if result.multi_hand_landmarks is not None:
        res = result.multi_hand_landmarks[0]        
        joint = np.zeros((21,3))
        for j, lm in enumerate(res.landmark):
            joint[j] = [lm.x, lm.y, lm.z]
        
        v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19,0,0,0,0,0],:]
        v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,4,8,12,16,20],:]

        v = v2 - v1
        v = v / np.linalg.norm(v, axis =1)[:, np.newaxis]
        compareV1 = v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,20,20,20],:]
        compareV2 = v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19,21,22,23,24],:]
        angle = np.arccos(np.einsum('nt, nt->n', compareV1, compareV2))
        return angle
    else:return None
def angles2(img):
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result=hands.process(imgRGB)
    
    if result.multi_hand_landmarks is not None:
        res = result.multi_hand_landmarks[0]        
        joint = np.zeros((21,3))
        for j, lm in enumerate(res.landmark):
            joint[j] = [lm.x, lm.y, lm.z]
        
        v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:]
        v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:]

        v = v2 - v1
        v = v / np.linalg.norm(v, axis =1)[:, np.newaxis]
        compareV1 = v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:]
        compareV2 = v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:]
        angle = np.arccos(np.einsum('nt, nt->n', compareV1, compareV2))
        return angle
    else:return None

video = cv2.VideoCapture(file)
arr=[]
if video.isOpened():
    while True:
        status, frame = video.read()
        if status:
            d=angles(frame)
            d2=angles2(frame)
            if (d is not None) and (d2 is not None):
                d = torch.tensor(d).float().to(device)
                d2 = torch.tensor(d2).float().to(device)
                output = model(d).squeeze()+model2(d2).squeeze()
                pred = torch.argmax(output).item()+1
                arr.append(pred)
                cv2.putText(frame,'%d'%pred,(50,50),cv2.FONT_HERSHEY_PLAIN,3,(0, 0, 255),2,cv2.LINE_AA,)
            cv2.imshow("test", frame)
            cv2.waitKey(1)
        else:break
else:
    print("Could not open video")
    exit()
video.release()
cv2.destroyAllWindows()

f = open("asl_numbers.txt", 'w')
for i in range(len(arr)):
    f.write('Frame %d, the number is: %d\n\n'%(i+1,arr[i]))

f.close()