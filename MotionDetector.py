import cv2, time

# This is used to store the first image seen by the camaera and
# acts as a reference for following images to be compared against
reference_frame = None

# # starts the camera, argument should  be changed if multiple cameras are available
video=cv2.VideoCapture(0)

while True:

    # captures boolean and numpy array from camera
    check, frame = video.read()

    # converts image to a gray version for more accuracy later on
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray, (21, 21,), 0) # smooths edges and reduces noise in calculations

    #checks to see if we need to assign the reference frame a value
    if reference_frame is None:
        reference_frame = gray
        continue

    # calculates diffeence between reference_frame and current fram and stores as an image
    delta_frame=cv2.absdiff(reference_frame, gray)

    # makes any pixel with a difference larger than athreshold white, else black
    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame, None,iterations=2)

    # finds conours of distinct objects in the frame
    (_,cnts,_)=cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # displays images
    cv2.imshow("Threshold", thresh_frame)
    cv2.imshow("Delta", delta_frame)
    cv2.imshow("Gray Frame", gray)

    # if q is pressed then loop is exited
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
