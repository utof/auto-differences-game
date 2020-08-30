from pyautogui import *
import pyautogui 	
import time
from PIL import Image, ImageChops, ImageDraw, ImageOps
import keyboard
import os
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


print('ready to take photos')

width1 = 340
height1 = 500

posx11 = 671
posx12 = 1021

posy11 = 342
posy12 = 342

biasx1 = 40
biasy1 = 40
while keyboard.is_pressed('e') == False:
    if keyboard.is_pressed('q') == True:
        img1 = pyautogui.screenshot(region=(posx11,posy11,width1,height1))
        img1.save(r"U:\Desktop\asdasd\research\tests\img1.jpg")

        img2 = pyautogui.screenshot(region=(posx12,posy12,width1,height1))
        img2.save(r"U:\Desktop\asdasd\research\tests\img2.jpg")


        img1=Image.open("img1.jpg")
        img2=Image.open("img2.jpg")

        diff=ImageChops.difference(img1,img2)
        print(diff.getbbox())
        ImageDraw.Draw(diff)
        diff = ImageOps.invert(diff)
        diff.save('ok.jpg')
        #os.startfile('ok.jpg')
        for x in range(biasx1, width1, 15):
            for y in range(biasy1, height1, 15):
                r,g,b = diff.getpixel((x, y))
                if (r in range(0,210)) or (g in range(0,210)) or (b in range(0,210)):
                    win32api.SetCursorPos((x + posx11, y + posy11))
                    time.sleep(0.05)
        print("done clicking")
        #create прохождение по кадрам. Нажал стрелку вправо, переходит к следющему
        #пикселю. Нажал вправо - вернулось обратно. Нажал энтер - кликнуло
        
        # Создай норм кнопку отключения скрипта, а то пздц!
        
        #Распознование отличающихся от белого фона объектов?
        #мб сделать что если несколько пикселей в округе  
        #попадают под range, то скипать все эти итерации(за счет одной) ?
        # а если заюзать свёртки? неполностью, но что б хотя бы
        # понимать как смотреть чуваков в округе!!!!
        

    if keyboard.is_pressed('a') == True:
        width2 = 687
        height2 = 242
        img1 = pyautogui.screenshot(region=(653,347,width2,height2))
        img1.save(r"U:\Desktop\asdasd\research\tests\img1.jpg")

        img2 = pyautogui.screenshot(region=(653,602,width2,height2))
        img2.save(r"U:\Desktop\asdasd\research\tests\img2.jpg")


        img1=Image.open("img1.jpg")
        img2=Image.open("img2.jpg")

        diff=ImageChops.difference(img1,img2)
        print(diff.getbbox())
        ImageDraw.Draw(diff)
        diff = ImageOps.invert(diff)
        diff.save('ok.jpg')
        os.startfile('ok.jpg')
            

print('done')


#invert the diff -- done

#"a" makes diff between long photos  -- done!!!!!
