import cv2, time

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    faces=face_cascade.detectMultiScale(frame,
    scaleFactor=1.05,
    minNeighbors=5)
    for x, y, width, height in faces:
        frame=cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 0, 255), 2)

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
