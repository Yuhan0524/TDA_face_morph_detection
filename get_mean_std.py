from sys import stderr
import matplotlib.pyplot as plt
import math
import numpy as np

def gd(x, mu, sigma):
    left = 1 / (np.sqrt(2 * math.pi) * np.sqrt(sigma))
    right = np.exp(-(x - mu)**2 / (2 * sigma))
    return left * right
def draw(mean1,std1,mean2,std2):
    x = np.arange(0, 30, 0.1)
    #  因变量（不同均值或方差）
    y_1 = gd(x, mean1, std1)
    y_2 = gd(x, mean2, std2)

    #  绘图
    plt.plot(x, y_1, color='green')
    plt.plot(x, y_2, color='blue')
    #  设置坐标系
    plt.xlim(-5, 35.0)
    plt.ylim(-0.2, 0.5)

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    plt.legend(labels=['$\mu$ = '+str(mean1)+', $\sigma^2$ = '+str(std1) , '$\mu$ = '+str(mean2)+', $\sigma^2$ = '+str(std2)])
    plt.show()


    
morph = [[14, 10, 8, 12, 11, 12, 15, 17],[17, 14, 7, 8, 7, 15, 9, 9],[6, 7, 10, 11, 13, 19, 18, 7],[23, 17, 13, 14, 13, 13, 19, 18],[15, 15, 12, 15, 17, 18, 14, 18],[27, 8, 8, 15, 17, 18, 25, 17],[11, 10, 8, 7, 15, 9, 22, 14],[16, 15, 12, 10, 3, 16, 19, 17],[20, 11, 5, 10, 10, 13, 18, 11],[20, 8, 7, 10, 10, 7, 20, 11]]
origin = [[17, 18, 16, 11, 10, 19, 31, 21],[16, 13, 13, 18, 23, 13, 22, 18],[17, 14, 13, 16, 16, 21, 17, 24],[15, 19, 13, 21, 16, 20, 23, 31],[16, 15, 23, 26, 18, 20, 20, 17],[19, 19, 17, 27, 18, 25, 28, 35],[24, 24, 16, 22, 16, 31, 29, 23],[10, 9, 8, 15, 10, 19, 31, 13],[18, 15, 15, 9, 10, 18, 23, 21],[15, 18, 9, 11, 14, 17, 24, 26]]

binary = [192,96,48,24,12,6,3,129]
for i in range(8):
  data = []
  data2 = []
  for j in range(10):
    data.append(morph[j][i])
    data2.append(origin[j][i])
  mean1 = sum(data)/10
  STD1 = np.std(np.array(data), ddof = 1)
  mean = sum(data2)/10
  STD = np.std(np.array(data2), ddof = 1)
  print("origin"+str(binary[i])+": mean = ",mean,"std = ",STD)
  print("morph"+str(binary[i])+": mean = ",mean1,"std = ",STD1)
  draw(mean,STD,mean1,STD1)