import cv2
import numpy as np
import numpy.random as nr
from scipy import signal
import itertools

w = 6
h = 5
bomb_rate = 0.12
cell_size = 60
nr.seed() #モジュール(関数)
number_c = [(255, 0, 0,), (0, 128, 0), (0, 0, 255), (128, 0, 0), (128, 128, 0), (0, 0, 0), (128, 128, 128)]

bomb_num = int(w * h * bomb_rate)
safe_num = w * h - bomb_num
#numpy.random モジュール内の permutation() 関数を使用してランダムな並び替え
bomb = nr.permutation([1]*bomb_num + [0]*safe_num).reshape(h, w).astype(bool)
print('bomb:\n{}'.format(bomb))

f = np.array([[1, 1, 1], 
             [1, 0, 1],
             [1, 1, 1]], int)
number = signal.convolve2d(bomb, f, mode='same', boundary='fill', fillvalue=0)
print('number:\n{}'.format(number))

clear = np.zeros((h, w), bool)
print('clear:\n{}'.format(clear))

flag = np.zeros((h, w), bool)
print('flag:\n{}', format(flag))

def make_img(extratext=''):
    img= np.zeros((h,w,3), 'unit8')
    img[~clear] = [190]*3
    img[clear] = [160]*3
    img = img.repeat(cell_size, axis=0).repeat(cell_size, axis=1)
    img[::cell_size, :] = [50]*3
    img[:, ::cell_size] = [50]*3

    font_size = cell_size * 0.02
    x_shift, y_shift = cell_size // 4, cell_size - (cell_size // 4)
    for i,j in itertools.product(range(h), range(w)):
        if flag[i, j]:
            cv2.putText(img, '+', cell_size*j+x_shift, cell_size*j+y_shift, cv2.FONT_HERSHEY_TRIPLEX, font_size, [0]*3, 2)
            continue
        if not clear[i, j] or number[i, j] == 0:
            continue
        cv2.putText(img, str(number[i, j]), (cell_size*j+x_shift, cell_size*j+y_shift), cv2.FONT_HERSHEY_TRIPLEX, font_size, number_c[number[i, j]-1], 2)

    if len(extract) > 0:
        for i, j in itertools.product(range(h), range(w)):
            if bomb[i, j]:
                cv2.putText(img, '@', (cell_size*j+x_shift, cell_size*j+x_shift), cv2.FONT_HERSHEY_TRIPLEX, font_size, (0, 0, 255), 2)
        cv2.putText(img, extratext, (cell_size*0+x_shift, cell_size*0+y_shift), cv2.FONT_HERSHEY_TRIPLEX, font_size, (0, 0, 0), 2)
    return img

def put_flag(i, j):
    global flag
    print('put_flag:({}, {})'.fotmat(j, i))