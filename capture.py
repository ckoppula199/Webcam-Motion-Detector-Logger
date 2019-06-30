import cv2, time

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)

fr = 1

while True:
    fr+=1
    check, frame = video.read()
    faces=face_cascade.detectMultiScale(frame,
    scaleFactor=1.1,
    minNeighbors=5)
    for x, y, width, height in faces:
        frame=cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 0, 255), 3)

    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print(fr)
video.release()
cv2.destroyAllWindows()
