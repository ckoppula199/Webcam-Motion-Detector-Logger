# Webcam-Motion-Detector-Logger

This porgram makes use of the OpenCV library. It firsts launches the webcam then waits 2 seconds to allow the camera to adjust to the environmental conditions. It then takes an image of the background to act as a reference frame. From here on every frame the webcam captures will be proccessed. First it is converted to grayscale then a guassian blur is applied, both to increase accuracy later on. The frame is then compared to the reference frame and any differences significant enough are recorded and displayed, a rectangle outlining the detected object appears and status changes from "No object detected" to "Object detected". If an Object is detected then the time it was first detected and the time it is no longer detected is recorded in a pandas dataframe which is then converted to a csv file. This csv file is then used to create a visualisation of when objects appeared in the frame. The visulisation uses the Bokeh library.

It is crucial that no moving objects are in frame for the first 2 seconds once the application has been launched in order to not mess up the reference frame.
