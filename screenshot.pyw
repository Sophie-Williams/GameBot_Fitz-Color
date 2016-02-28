
from PIL import ImageGrab
import os
import time

# global
#==========
x_pad = 459
y_pad = 100

def snapShot():
    box = (x_pad+1, y_pad+1, x_pad+445, y_pad+667)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\actual_snap_' + str(int(time.time())) + '.png', 'PNG')

def main():
    snapShot()

if __name__ == '__main__':
    main()
