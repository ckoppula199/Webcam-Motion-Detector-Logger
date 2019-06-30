import cv2, time

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#face_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")
#face_cascade=cv2.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
#face_cascade=cv2.CascadeClassifier("haarcascade_lefteye_2splits.xml")
#face_cascade=cv2.CascadeClassifier("haarcascade_smile.xml")
video=cv2.VideoCapture(0)

fr = 1
start = time.time()
while True:
    fr+=1
    check, frame = video.read()
    faces=face_cascade.detectMultiScale(frame,
    scaleFactor=1.05,
    minNeighbors=5)
    for x, y, width, height in faces:
        frame=cv2.rectangle(frame, (x,y), (x+width, y+height), (0, 0, 255), 2)

    #gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
end = time.time()

time_taken = end - start
minutes = time_taken / 60
frame_rate = fr/minutes/60
print("Framerate was " + str(frame_rate) + " frames per second")
video.release()
cv2.destroyAllWindows()
