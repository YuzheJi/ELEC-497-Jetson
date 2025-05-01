import cv2
import numpy as np
from ultralytics import YOLO

# main program
print('Program start')
model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # system camera

# capture a frame and show
while True:
    reg, frame = cap.read()
    frame = cv2.flip(frame, 1)      # required to flip left and right 
    cv2.imshow('camera', frame) 

    filename = 'frame.png' 
    cv2.imwrite(r'D:\University\Year 2-s Term 1\ELEC 497 Jetson Nano\camera file' + '\\' + filename, frame)
    print(filename + ' is saved') 
      
    results = model(r"D:\University\Year 2-s Term 1\ELEC 497 Jetson Nano\camera file\frame.png")  
    frame_anoted = results[0].plot()
    cv2.imshow('detection', frame_anoted) 
    #results[0].show()  # 显示结果
    
    # press q to exit
    if cv2.waitKey(1) & 0xff == ord('q'):
      break