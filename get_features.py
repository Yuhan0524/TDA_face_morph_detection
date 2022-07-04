import numpy as np
import gudhi
import gudhi.representations
import cv2
from skimage.feature import local_binary_pattern

def img_gray(path):
  img = cv2.imread(path)
  h,w = img.shape[:2] #获取图片的high和wide
  img_gray=np.zeros([h,w],img.dtype) #创建一张和当前图片大小一样的单通道图片
  for i in range(h):
      for j in range(w):
          m = img[i,j]
          img_gray[i,j] =int(m[0]*0.11+m[1]*0.59+m[2]*0.3) #将BGR坐标转换为gray坐标
  return img_gray


def lbp(pixels):

  features = []
  img = pixels.tolist()
  lbp = local_binary_pattern(img, 8, 1, "default")
  binary = [192,96,48,24,12,6,3,129]
  for k in range(8):
    point_position = []
    dgms_normal = []
    for i in range(256):
      for j in range(256):
        if lbp[i][j] == binary[k]:
          point_position.append([j,i])
    normal_pcs = point_position
    rips = gudhi.RipsComplex(points=normal_pcs).create_simplex_tree(max_dimension=2)
    rips.compute_persistence()
    dgms_normal.append(rips.persistence_intervals_in_dimension(1))
    matrix = dgms_normal[0]
    data = matrix.tolist()
    if data == []:
      features.append(0)
    else:
      count=0
      for i in range(len(data)):
        if 20 <= data[i][1] and 20 >= data[i][0]:
          count+=1
      features.append(count)
  return features

for i in range(1,11):
  path = "/content/drive/MyDrive/Colab Notebooks/"+str(i)+".tiff"
  pixels = img_gray(path)
  print(lbp(pixels))

for i in range(1,11):
  path = "/content/drive/MyDrive/Colab Notebooks/morph"+str(i)+".png"
  pixels = img_gray(path)
  print(lbp(pixels))