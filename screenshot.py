
from PIL import ImageGrab
import os
import time
from PIL import ImageOps
from numpy import *

# global
#==========
x_pad = 467
y_pad = 84

if not os.path.exists(os.getcwd() + '\\images'):    
    os.makedirs(os.getcwd() + '\\images')

def snapShot():     # it was used for setting the co-ordinate of the game
    box = (x_pad+1, y_pad+1, x_pad+429, y_pad+640)
    im = ImageGrab.grab(box)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\images\\actual_snap_' + str(int(time.time())) + '.png', 'PNG')

def titleColor():
    box = (x_pad+101, y_pad+94, x_pad+191, y_pad+160)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_1():
    box = (x_pad+160, y_pad+220, x_pad+300, y_pad+280)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_2():
    box = (x_pad+160, y_pad+370, x_pad+300, y_pad+430)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_3():
    box = (x_pad+160, y_pad+510, x_pad+300, y_pad+570)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def main():
    pass

if __name__ == '__main__':
    main()
