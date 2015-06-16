# -*- coding: utf-8 -*-
import time
from PIL import Image
import os, win32gui, win32ui, win32con, win32api
import time

# dpath is the path of the image
# return the name of image
def window_capture(dpath):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None,None)
    # width and height of image
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
    cc = time.gmtime()
    bmpname = str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'.bmp'
    saveBitMap.SaveBitmapFile(saveDC, bmpname)
    Image.open(bmpname).save(bmpname[:-4]+".jpg")
    os.remove(bmpname)
    jpgname = bmpname[:-4]+'.jpg'
    djpgname = dpath + jpgname
    copy_command = "move %s %s" % (jpgname, djpgname)
    os.popen(copy_command)
    return bmpname[:-4]+'.jpg'