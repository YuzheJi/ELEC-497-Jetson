import cv2

print("program start")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("no stream!")
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        print("window closed by user")
        break
cap.release()
cv2.destroyAllWindows()
