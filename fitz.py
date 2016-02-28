from PIL import ImageGrab
import os
import time
from PIL import ImageOps
from numpy import *
import win32api, win32con

# Global
# --------
x_pad = 459
y_pad = 100

def snapShot():
    box = (x_pad+1, y_pad+1, x_pad+445, y_pad+667)
    im = ImageGrab.grab(box)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\actual_snap_' + str(int(time.time())) + '.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print 'CLICK'

def mousePos(cord):
    win32api,SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

color_text = {
    37950: 'green',
    38061: 'gray',
    37311: 'purple',
    38545: 'red',
    37380: 'blue'
    }

color_color = {
    8579: 'green',
    8606: 'gray',
    8572: 'blue',
    8568: 'purple',
    8593: 'orange',
    8536: 'red'
    }

class Cord:
    play = (229, 250)
    
    first_box = (222, 269)
    second_box = (222, 412)
    third_box = (222, 554)
    

def writtenColor():
    box = (x_pad+149, y_pad+96, x_pad+251, y_pad+183)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
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
