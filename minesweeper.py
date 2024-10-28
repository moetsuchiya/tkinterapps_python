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
#
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
    for i,j in itertools.product(range(h), range(w)):#全セルの座標(i, j)を取得
        if flag[i, j]: #「旗（フラグ）」が立てられているかどうか
            cv2.putText(img, '+', cell_size*j+x_shift, cell_size*j+y_shift, cv2.FONT_HERSHEY_TRIPLEX, font_size, [0]*3, 2)
            continue
        if not clear[i, j] or number[i, j] == 0: #clear: 「クリア済み」であるかどうか
            continue #number: セル(i, j)に隣接する地雷（爆弾）の数
        cv2.putText(img, str(number[i, j]), (cell_size*j+x_shift, cell_size*j+y_shift), cv2.FONT_HERSHEY_TRIPLEX, font_size, number_c[number[i, j]-1], 2)

    if len(extratext) > 0:
        for i, j in itertools.product(range(h), range(w)):
            if bomb[i, j]:
                cv2.putText(img, '@', (cell_size*j+x_shift, cell_size*j+x_shift), cv2.FONT_HERSHEY_TRIPLEX, font_size, (0, 0, 255), 2)
        cv2.putText(img, extratext, (cell_size*0+x_shift, cell_size*0+y_shift), cv2.FONT_HERSHEY_TRIPLEX, font_size, (0, 0, 0), 2)
    return img

def put_flag(i, j):
    global flag
    print('put_flag:({}, {})'.fotmat(j, i))

    if clear[i, j] or flag[i, j]:
        print(' -> Cannot flag here')
        return make_img()
    
    if not bomb[i, j]:
        print(' -> Game Over')
        return make_img(extratext='Game Over')
    
    flag[i, j] = True

    if (flag == bomb).all():
        print(' ->Success')
        return make_img(extratext='success!!')

def put_clear(i, j):
    global clear
    print('put_clear:({}, {})'.format(j, i))

    if clear[i, j] or flag[i, j]:
        print(' -> Cannot open here')
        return make_img()
    if bomb[i, j]:
        print(' -> Game Over')
        return make_img(extratext='Game Over')
    
    clear[i, j] = True

    if number[i, j] == 0:
        put_clear(np.clip(i - 1, 0, h - 1), np.clip(j - 1 , 0, w - 1))
        put_clear(np.clip(i - 1, 0, h - 1), np.clip(j, 0, w - 1))
        put_clear(np.clip(i - 1, 0, h - 1), np.clip(j + 1 , 0, w - 1))
        put_clear(np.clip(i, 0, h - 1), np.clip(j - 1 , 0, w - 1))
        put_clear(np.clip(i, 0, h - 1), np.clip(j + 1 , 0, w - 1))
        put_clear(np.clip(i + 1, 0, h - 1), np.clip(j - 1 , 0, w - 1))
        put_clear(np.clip(i + 1, 0, h - 1), np.clip(j, 0, w - 1))
        put_clear(np.clip(i + 1, 0, h - 1), np.clip(j + 1 , 0, w - 1))

    if (clear == ~bomb).all():
        print(' -> Success')
        return make_img(rxtratext='Success!!')
    
    return make_img()

def onMouse(event, x, y, flgs, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        i, j = y//cell_size, x//cell_size
        img = put_clear(i, j)
        cv2.imshow(wname, img)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        i, j = y//cell_size, x//cell_size
        img = put_flag(i, j)
        cv2.imshow(wname, img)

img = make_img()

wname = 'Minesweeper'
cv2.nameWindow(wname)
cv2.setMouseCallback(wname, onMouse)

cv2.imshow(wname, img)
cv2.waitKey()