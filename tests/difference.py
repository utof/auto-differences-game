import pyautogui 	
import time
from PIL import Image, ImageChops, ImageDraw, ImageOps
import keyboard
import os

while keyboard.is_pressed('e') == False:
    if keyboard.is_pressed('q') == True:
        img1 = pyautogui.screenshot(region=(651,342,340,500))
        img1.save(r"U:\Desktop\asdasd\research\tests\img1.jpg")

        img2 = pyautogui.screenshot(region=(1001,342,340,500))
        img2.save(r"U:\Desktop\asdasd\research\tests\img2.jpg")


        img1=Image.open("img1.jpg")
        img2=Image.open("img2.jpg")

        diff=ImageChops.difference(img1,img2)
        print(diff.getbbox())
        ImageDraw.Draw(diff)
        diff = ImageOps.invert(diff)
        diff = Image.blend(diff, img1, 0.045)
        diff.save('ok.jpg')
        os.startfile('ok.jpg')

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
        diff = Image.blend(diff, img1, 0.05)
        diff.save('ok.jpg')
        os.startfile('ok.jpg')
            

print('done')


#invert the diff -- done

#"a" makes diff between long photos  -- done!!!!!
