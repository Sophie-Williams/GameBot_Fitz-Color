""" 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
x_pad = 459
y_pad = 100
Play area =  x_pad+1, y_pad+1, 904, 767
"""

from PIL import ImageGrab
import os
import time
from PIL import ImageOps
from numpy import *
import win32api, win32con
from Tkinter import *

if not os.path.exists(os.getcwd() + '\\images'):    
    os.makedirs(os.getcwd() + '\\images')

def snapShot():     
    box = (x_pad+1, y_pad+1, x_pad+445, y_pad+667)
    im = ImageGrab.grab(box)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\images\\actual_snap_' + str(int(time.time())) + '.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.99)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print 'CLICK'

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

class Cord:                 
    play = (229, 250)
    first_box = (222, 269)
    second_box = (222, 412)
    third_box = (222, 554)
    
def titleColor():
    box = (x_pad+149, y_pad+96, x_pad+251, y_pad+183)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print a
    # im.save(os.getcwd() + '\\image\\title_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_1():
    box = (x_pad+160, y_pad+240, x_pad+300, y_pad+300)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    # print a
    # im.save(os.getcwd() + '\\image\\box_1_snap' + str(int(time.time())) + '.png', 'PNG')     # for debugging
    return a

def colorBox_2():
    box = (x_pad+160, y_pad+370, x_pad+300, y_pad+430)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    # print a
    # im.save(os.getcwd() + '\\image\\box_2_snap' + str(int(time.time())) + '.png', 'PNG')     # for debugging
    return a

def colorBox_3():
    box = (x_pad+160, y_pad+520, x_pad+300, y_pad+580)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    # print a
    # im.save(os.getcwd() + '\\box_3_snap' + str(int(time.time())) + '.png', 'PNG')     # for debugging
    return a

def Go():
    for xx in color_text:
        if titleColor() == xx:
            dd = color_color[color_text[xx]]
            break
    dd = color_color[color_text[xx]]
    if dd == colorBox_1():
        # click first box
        mousePos(Cord.first_box)
        leftClick()
        print 'first'
        #time.sleep(.1)
        return
    elif dd == colorBox_2():
        # click second oox
        mousePos(Cord.second_box)
        leftClick()
        print 'second'
        #time.sleep(.1)
        return
    elif dd == colorBox_3():
        # click third box
        mousePos(Cord.third_box)
        leftClick()
        print 'third'
        #time.sleep(.1)
        return

def gui():
    gui_d = Tk()
    gui_d.geometry('200x100+800+400')
    gui_d.title("Fitz-Color Bot")
    gui_d.mainloop()
    label_1 = Label(gui_d,text = 'Enter the Score').pack()
    button_1 = Button(gui_d, text = "OK", command = pass_text()).pack()

    def pass_text():
        return label_1.text

    

def start():
    for x in range(0,130):
        Go()
        time.sleep(.019)
#---------------------------------------------------------------------------------
        
# Global
# --------
x_pad = 459
y_pad = 100

color_text = {
    37950: 'green',
    38061: 'gray',
    37380: 'blue',
    37311: 'purple',
    37783: 'orange',
    38545: 'red'
    }

color_color = {
    'green':8579,
    'gray':8609,
    'blue':8572,
    'purple':8568,
    'orange':8593,
    'red':8536
    }

def main():
    pass

if __name__ == '__main__':
    main()
