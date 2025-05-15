from ultralytics import YOLO 
import cv2
import torch 
import time 

def warmup_model(model, input_size=(640, 640), device='cuda', repeat=3):
    dummy = torch.zeros((1, 3, input_size[0], input_size[1])).to(device)
    with torch.no_grad():
        for i in range(repeat):
            start = time.time()
            model(dummy)
            print(f"Warmup run {i+1} took {time.time() - start:.4f} seconds")
        print("GPU warm-up DONE!")

print("Program start, press q to exit...")
cap = cv2.VideoCapture(0)
model = YOLO("yolo11n.engine")
filename = "frame.png"

print("Warming up GPU...")
warmup_model(model=model)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("no stream!")
        break

    cv2.imwrite(filename, frame)
    print(filename + ' is saved') 

    results = model(r"/home/jetson-ji/yolo11/frame.png")

    frame_anotated = frame_anoted = results[0].plot()

    cv2.imshow('Detection', frame_anotated)


    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
