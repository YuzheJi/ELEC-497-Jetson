from ultralytics import YOLO 
import cv2
import torch 
import time 
import os
from pathlib import Path

def warmup_model(model, input_size=(640, 640), device='cuda', repeat=3):
    print("🔧: Warming up GPU...")
    dummy = torch.zeros((1, 3, input_size[0], input_size[1])).to(device)
    with torch.no_grad():
        for i in range(repeat):
            start = time.time()
            model(dummy)
            print(f"Warmup run {i+1} took {time.time() - start:.4f} seconds")
        print("GPU warm-up DONE!")


print("🔧: Starting the program...")
time.sleep(1)
print("🔧: Initialzing YOLO model, taking default choice (yolo11n.engine)")
time.sleep(1)
model_name='yolo11n.engine'
print("🔧: Checking Camera connection...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌: Cannot open camera")
    exit()
print("✅: Camera is connected!")

dir_name = Path.cwd()
model = YOLO("yolo11n.engine", task='detect')
warmup_model(model=model)

while True:
    ret, frame = cap.read()
    if not ret:
        print("no stream!")
        break

    results = model(frame)
    frame_anotated = frame_anoted = results[0].plot()
    cv2.imshow('Detection', frame_anotated)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
