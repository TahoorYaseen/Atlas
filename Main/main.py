import dety4 as dt
import dety4E as dtE
import dety4S as dtS
import dety4W as dtW
gtime = 0
import time
import cv2 
import os

while True:
    # if os.path.isfile("test4North.jpg"):
    #     os.remove("test4North.jpg")
    # capNorth = cv2.VideoCapture("videoNorth.mp4")
    # imgNorth = capNorth.read()
    # cv2.imwrite("test4North.jpg",imgNorth)
    exec(open("dety4.py").read())
    gtime = dt.green_time
    print(f"green for north side for {gtime} seconds")
    time.sleep(gtime-5)
    # capEast = cv2.VideoCapture("videoEast.mp4")
    # imgEast = capE.read()
    # cv2.imwrite("test4East.jpg",imgEast)
    exec(open("dety4E.py").read())
    gtime = dtE.green_time
    time.sleep(5)

    print("RED for north side\n")
    print(f"\ngreen for east side for {gtime} seconds")
    time.sleep(gtime-5)
    # capSouth = cv2.VideoCapture("videoSouth.mp4")
    # imgSouth = capE.read()
    # cv2.imwrite("test4South.jpg",imgSouth)
    exec(open("dety4S.py").read())
    gtime = dtS.green_time
    time.sleep(5)

    print("RED for east side")
    print(f"green for south side for {gtime} seconds")
    time.sleep(gtime-5)
    # capWest = cv2.VideoCapture("videoWest.mp4")
    # imgWest = capWest.read()
    # cv2.imwrite("test4West.jpg",imgWest)
    exec(open("dety4W.py").read())
    gtime = dtW.green_time
    time.sleep(5)

    print("RED for south side")
    print(f"green for west side for {gtime} seconds")
    time.sleep(gtime)
    print("REd for west side ")

