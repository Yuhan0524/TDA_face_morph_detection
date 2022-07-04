# -*- coding: utf-8 -*-
"""
Created on Tue May 31 22:54:40 2022

@author: 27677
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 16 15:35:05 2022

@author: 27677
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:16:03 2022

@author: 27677
"""

# _*_ coding:utf-8 _*_

import numpy as np
import cv2
import dlib
import gudhi as gd
import gudhi.representations
import matplotlib.pyplot as plt

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_81_face_landmarks.dat')

# cv2 read the picture


# 取灰度
def get_data(path):
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
    # 人脸数rects
    rects = detector(img_gray, 0)
    dataset=[]
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img,rects[i]).parts()])
        for idx, point in enumerate(landmarks):
            # 81点的坐标
            pos =[point[0, 0], point[0, 1]]
            dataset.append(pos)
            # 利用cv2.circle给每个特征点画一个圈，共81个
            cv2.circle(img, pos, 5, color=(0, 255, 0))
            # 利用cv2.putText输出1-81
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(idx+1), pos, font, 0.8, (0, 0, 255), 1,cv2.LINE_AA)
    return dataset


for i in range(6,11):
    path = str(i)+".tiff"
    dataset = get_data(path)
    for j in range(68):
        print(dataset[j][0], end=' ')
        print(dataset[j][1], end='')
        print()
    print()
        
    log_file = open(str(i)+'.txt','a+')
    log_file.close()


'''
#--------------------------------------------------------------------------------
x=[0]*81
y=[0]*81
for i in range(len(dataset)):
    x[i]=dataset[i][0]
    y[i]=dataset[i][1]
plt.scatter(x,y,s=3)
plt.show()


acX = gd.AlphaComplex(points=dataset).create_simplex_tree()
dgmX = acX.persistence()
gd.plot_persistence_diagram(dgmX)
plt.show()
'''