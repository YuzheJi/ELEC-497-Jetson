from ultralytics import YOLO 
import cv2

print("Program start, press q to exit...")
cap = cv2.VideoCapture(0)
model = YOLO("yolo11n.engine")
filename = "frame.png"

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
