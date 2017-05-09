import pygame
import pygame.camera
import requests
import time
import sys
import math, operator
from PIL import ImageChops
from PIL import Image
from functools import reduce

DEBUGING = True
currentImage = 0
SIZE = (640, 480)
serverUrl = "http://hansohnadventures.com/iot/smartcam/postimage"
notifyUrl = "http://hansohnadventures.com/iot/smartcam/sendnotification"
saveFolder = "../webcam/image000"

def compareImg(imgOne, imgTwo):
    h1 = Image.open(saveFolder+str(imgOne)+".jpg").histogram()
    h2 = Image.open(saveFolder+str(imgTwo)+".jpg").histogram()
    err = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return err

def mse(imgOne, imgTwo):
    img1 = Image.open(saveFolder+str(imgOne)+".jpg")
    img2 = Image.open(saveFolder+str(imgTwo)+".jpg")
    h = ImageChops.difference(img1, img2).histogram()
    err = math.sqrt(reduce(operator.add, map(lambda h, i: h*(i**2), h, range(256))) / (float(img1.size[0]) * img1.size[1]))
    return err

def countDown(counter):
    for curCount in range(counter, 0, -1):
        sys.stdout.write(str(curCount))
        time.sleep(1)

def postImage():
    file = open(saveFolder+str(currentImage)+".jpg", 'rb')
    img = file.read()
    file.close()
    files = {'file': ("image000"+str(currentImage)+".jpg",img,'imge/jpeg')}
    printOut("Sending...", "debug")
    r = requests.post(serverUrl, files=files)
    printOut(str(r.status_code), "debug")
    printOut("Sent!", "debug")

def sendNotification():
    r = requests.get(notifyUrl)
    printOut(str(r.status_code), "debug")
    printOut("Sent!", "debug")
    
def takePicture():
    global currentImage
    img = cam.get_image()
    pygame.image.save(img, saveFolder+str(currentImage)+".jpg")
    postImage()
    if currentImage == 0:
        currentImage = 1
    else:
        currentImage = 0

def checkImages():
    err1 = compareImg(0, 1)
    err2 = mse(0, 1)
    printOut("err1: "+str(err1)+"err2: "+str(err2),"debug")
    if err1 > 500 and err2 > 25:
        sys.stdout.write("\n"+str(err1))
        sys.stdout.write("\n"+str(err2))
        return 1
    return 0

def printOut(message, level):
    if level != "debug" or DEBUGING:
        sys.stdout.write("\n"+message)

printOut("initializing...", "normal")
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", SIZE)
printOut("Staring cammera", "normal")
cam.start()
printOut("Running...", "normal")

takePicture()
for x in range(0,100):
    takePicture()
    if checkImages() == 1:
        sendNotification()
    #countDown(5)
printOut("Stopping...", "normal")
cam.stop()
printOut("All done!", "normal")

