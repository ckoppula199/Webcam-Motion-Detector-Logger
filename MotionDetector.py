import cv2, time, pandas, imutils
from imutils.video import VideoStream
from datetime import datetime

# This is used to store the first image seen by the camaera and
# acts as a reference for following images to be compared against
reference_frame = None
status_list = [None, None] # list needs 2 initial items
times = []
df=pandas.DataFrame(columns=["Start", "End"])

#starts the camera, argument should  be changed if multiple cameras are available
#video=cv2.VideoCapture(0) # alternate way of accessing camera but I've found it not to be as good
video = VideoStream(src=0).start()
time.sleep(2.0) #gives camera time to adjust to envronmental conditions

while True:


    # captures boolean and numpy array from camera
    #check, frame = video.read() # if using cv2.VideoCapture(0) then uncomment this and comment the below statement
    frame = video.read()
    text = "No Movement Detected"

    status = 0
    # converts image to a gray version for more accuracy later on
    frame = imutils.resize(frame, width=500)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21,), 0) # smooths edges and reduces noise in calculations

    #checks to see if we need to assign the reference frame a value
    if reference_frame is None:
        reference_frame = gray
        continue


    # calculates diffeence between reference_frame and current fram and stores as an image
    delta_frame=cv2.absdiff(reference_frame, gray)

    # makes any pixel with a difference larger than athreshold white, else black
    thresh_frame=cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1] #adjust second argument to change the difference required for a pixel to be classed as moving
    thresh_frame=cv2.dilate(thresh_frame, None,iterations=2)


    # finds contours of distinct objects in the frame
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # if object has area greater than 500 pxls then it is highlighted
    for contour in cnts:
        if cv2.contourArea(contour) < 500: # change value based on size of object trying to detect
            continue
        status = 1

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2) #draw rectangle
        text = "Motion Detected"

    #saves space as we only need the last 2 values to check a change in status
    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0: #object has been detected
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1: #object is no longer being detected
        times.append(datetime.now())


    # adds text overlay of current status and time
    cv2.putText(frame, "Status: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0 , 255), 1)

    # displays images
    cv2.imshow("Gray", gray)
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("frame", frame)

    # if q is pressed then loop is exited
    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")

#video.release()
video.stop()
cv2.destroyAllWindows()
