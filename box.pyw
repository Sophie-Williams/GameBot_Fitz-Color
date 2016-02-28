
from PIL import ImageGrab
import os
import time
from PIL import ImageOps
from numpy import *

#Glabal
# ==========
x_pad = 459
y_pad = 100

def snapShot():
    box = (x_pad+1, y_pad+1, x_pad+445, y_pad+667)
    im = ImageGrab.grab(box)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\actual_snap_' + str(int(time.time())) + '.png', 'PNG')

def written():
    box = (x_pad+149, y_pad+96, x_pad+251, y_pad+183)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def tar(a,b,c,d):
    box = (x_pad+a, y_pad+b, x_pad+c, y_pad+d)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\tar_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_1():
    box = (x_pad+160, y_pad+240, x_pad+300, y_pad+300)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_2():
    box = (x_pad+160, y_pad+370, x_pad+300, y_pad+430)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_3():
    box = (x_pad+160, y_pad+520, x_pad+300, y_pad+580)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a
    
    


def main():
    pass

if __name__ == '__main__':
    main()
