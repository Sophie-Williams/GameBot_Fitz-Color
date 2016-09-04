""" 
All coordinates assume a screen resolution of 1280x1024, and Chrome 
maximized with the Bookmarks Toolbar enabled.
with Task bar at the bottom
Operating System: Windows 10
x_pad = 459
y_pad = 100
Play area =  x_pad+1, y_pad+1, 904, 758
Precaution: don't move cursor while bot is running,
bot might get disturbed :P
"""

from PIL import ImageGrab
import os
import time
from PIL import ImageOps
from numpy import *
import win32api, win32con
import tkinter as tk

# Global
# --------
x_pad = 459
y_pad = 91

def snapShot():
    box = (x_pad+1, y_pad+1, x_pad+445, y_pad+667)
    im = ImageGrab.grab(box)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\actual_snap_' + str(int(time.time())) + '.png', 'PNG')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.095)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('CLICK')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,y)

color_text = {
    34400: 'green',
    33211: 'gray',
    32215: 'blue',
    32415: 'purple',
    35498: 'orange',
    30465: 'red'
    }

color_color = {
    'green':8579,
    'gray':8609,
    'blue':8572,
    'purple':8568,
    'orange':8593,
    'red':8536
    }

class Cord:
    
    first_box = (222, 240)
    second_box = (222, 380)
    third_box = (222, 524)
    

def titleColor():
    box = (x_pad+109, y_pad+87, x_pad+199, y_pad+153)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    # im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_1():
    box = (x_pad+160, y_pad+220, x_pad+300, y_pad+280)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    # im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_2():
    box = (x_pad+160, y_pad+370, x_pad+300, y_pad+430)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    # im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
    return a

def colorBox_3():
    box = (x_pad+160, y_pad+510, x_pad+300, y_pad+570)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print (a)
    # im.save(os.getcwd() + '\\actual_snap' + str(int(time.time())) + '.png', 'PNG')
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
        print ('first')
        #time.sleep(.1)
        return
    elif dd == colorBox_2():
        # click second oox
        mousePos(Cord.second_box)
        leftClick()
        print ('second')
        #time.sleep(.1)
        return
    elif dd == colorBox_3():
        # click third box
        mousePos(Cord.third_box)
        leftClick()
        print ('third')
        #time.sleep(.1)
        return


def start(a):
    for x in range(0,int(a)):
        Go()
        time.sleep(.022)

class Gpic(tk.Tk):
    def  __init__(self):
        tk.Tk.__init__(self)
        self.title("Bot")
        self.iconbitmap(os.getcwd() + '\\images\\Virus.ico')
        self.geometry("315x225+950+400")
        self.resizable(width=tk.FALSE, height=tk.FALSE)
        self.lbl = tk.Label(self, text = "Enter the score")
        self.lbl.grid()
        self.entry = tk.Entry(self)
        self.entry.grid()
        self.btn = tk.Button(self, text="Ok", command = self.click)
        self.btn.grid()
        self.lbl2_message = tk.Label(self, text = """
* Operating System: Windows 10 or 8.1
* All coordinates assume a screen resolution of 1280x1024.
* Chrome maximized with the Bookmarks Toolbar enabled.
* Task bar at the bottom
* x_pad = 459 and y_pad = 100
* Play area =  x_pad+1, y_pad+1, 904, 758
* Precaution: don't move cursor while bot is running,
  bot might get disturbed :P
""")
        self.lbl2_message.grid(sticky=tk.W)

    def click(self):
        start(self.entry.get())
        self.destroy()
        
def main():
    app = Gpic()
    app.mainloop()

if __name__ == '__main__':
    main()
    
