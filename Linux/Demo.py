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
        print("✅: GPU warm-up DONE!")

def dir_search(dir_name, extensions):
    for ext in extensions:
        file_results.extend(dir_name.rglob(ext))
    for i, file in enumerate(file_results, start=1):
        relative_path = file.relative_to(dir_name)
        file_results[i-1] = str(relative_path)
        print(f"{i}. {file_results[i-1]}")
    print("----------------------")

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

filename = "frame.png"
dir_name = Path.cwd()
file_results = []
extensions_full = ["*.pt", "*.onnx", "*.engine"]
extensions_exp = ["*.pt"]

while True:
    time.sleep(1)
    print("\nThis is a demo for YOLO11 made by Ji, Terry and Emma")
    print("Current dir:"+str(dir_name))
    print("Using model: "+model_name)
    print("Select the following functions:")
    print("1. Select Model")
    print("2. Export to .engine file")
    print("3. Start detection")
    print("0. Exit")
    selection = input("Your selection: ") 

    time.sleep(1)
    if selection == '1':
        print("\n----------------------")
        print("Scanning dir: " + str(dir_name))
        bdone=False
        dir_search(dir_name=dir_name, extensions=extensions_full)
        print('\nCurrent Model: '+model_name)
        selection = input("Select from models above (0 for unchange): ")
        selection = int(selection)
        if selection == 0:
            time.sleep(1)
            print('Still using ' + model_name)
            file_results = []
            break
        model_name_new = file_results[selection-1]
        selection = input(f'Do you want {model_name_new} as your model (Y/N): ')
        if selection=='y' or selection == 'Y':
            model_name = model_name_new
            time.sleep(1)
            print('Now using ' + model_name)
        else:
            time.sleep(1)
            print('User cancelled, still using ' + model_name)
        file_results = []
 
    elif selection == '2':
        print("\n----------------------")
        print("Scanning dir: " + str(dir_name))
        time.sleep(1)
        print("Select the file you want to export:")
        dir_search(dir_name=dir_name, extensions=extensions_exp)
        selection = input("Select from models above: ")
        selection = int(selection)
        model_name_exp = file_results[selection-1]
        file_results = []
        selection = input(f'Do you want to export {model_name_exp} (Y/N): ')
        if selection == 'y' or selection == 'Y':
            time.sleep(1)
            print('🔧: Exporting '+ model_name_exp)
            model_exp = YOLO(model=model_name_exp, task='detect')
            model_exp.export(format='engine')
        else:
            time.sleep(1)
            print('User canceled the export process')

    elif selection == '3':
        print('🔧: Starting detection using '+ model_name)
        model = YOLO(model=model_name, task='detect')
        if model_name.endswith('.engine'):
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
        cv2.destroyAllWindows()

    elif selection == '0':
        print("User exit the program")
        break
    else:
        print("Unknown command...")
cap.release()
    

