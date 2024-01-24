import pyautogui
from playsound import playsound

def sound():
    playsound('beep-01a.mp3')    

wh = pyautogui.size()
print(wh.width, wh.height)

width_resolution_multiplier = 1440/wh.width
height_resolution_multiplier = 1080/wh.height
#top left 1251 207
#bottom right 1378 271
while True:
    pic = pyautogui.screenshot(region=(int(1280/width_resolution_multiplier),int(230/height_resolution_multiplier),int(120/width_resolution_multiplier),int(50/height_resolution_multiplier)))
    width, height = pic.size
    
    for x in range(0,int(120/width_resolution_multiplier)):
        for y in range(0,int(50/height_resolution_multiplier)):
            r,g,b = pic.getpixel((x,y))
            if (r,g,b) == (134,239,255):
                print("Blue!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                sound()
                break
                
