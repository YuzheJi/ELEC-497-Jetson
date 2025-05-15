import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
from ultralytics import YOLO
import os


class application:
    def __init__(self,root):
        self.root = root
        self.root.title("Computer Vision Demo")
        root.geometry("1300x700+10+50")
        self.model = YOLO("yolo11n.pt")
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # system camera
        self.label1 = tk.Label(root)
        self.label1.pack(pady=10, side='left')
        self.label2 = tk.Label(root)
        self.label2.pack(pady=10, side='left')
        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            filename = 'frame.png' 
            cv2.imwrite(r'camera file' + '\\' + filename, frame)
            print(filename + ' is saved') 
      
            results = self.model(r"camera file\frame.png")  
            frame_result = results[0].plot()
            img_result = Image.fromarray(frame_result)
            imgtk_result = ImageTk.PhotoImage(image=img_result)

            self.label1.imgtk = imgtk  
            self.label1.config(image=imgtk)

            self.label2.imgtk = imgtk_result  
            self.label2.config(image=imgtk_result)
        self.root.after(10, self.update_frame)
      
    def __del__(self):
        file_path = r"camera file\frame.png"

        if os.path.exists(file_path):
            os.remove(file_path)

        if self.cap.isOpened():
            self.cap.release()
print("Program Start")
root = tk.Tk()
app = application(root)
root.mainloop()
