import os
import pandas as pd
import numpy as np
import sklearn.preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from pandas import DataFrame
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


DATA_FOLDER_PATH = os.path.abspath("C:/Users/김한솔/Documents/겨울계절 자료")
TRAINING_DATASET = DATA_FOLDER_PATH + "/" + "train/test_landmarks.csv"

k_range = range(1,100)              # k를 1~100까지 고려하여 최적의 k를 찾을 것이다.
k_score = []                        # 각 k들의 성능을 비교하기 위한 리스트생성이다.

df = pd.read_csv(TRAINING_DATASET)
df = df.dropna()
X = np.array(df.drop(['target'],1))
Y = np.array(df['target'])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=1)

for k in k_range :
	model = KNeighborsClassifier(k)
	scores = cross_val_score(model,X,Y,cv=10,scoring = "accuracy")    # 10-fold cross-validation
	k_score.append(scores.mean())                    # 10-fold 각각 정확도의 평균으로 성능계산 


plt.plot(k_range, k_score)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validation Accuracy')
plt.show()