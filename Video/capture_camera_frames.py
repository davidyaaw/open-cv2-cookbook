import cv2

cameraCapture = cv2.VideoCapture(1)
fps = 30 #Произвольное по камере
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter(
    'output_vid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)

success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1 # 10 secs of frames
while success and numFramesRemaining > 0 :
    videoWriter.write(frame)
    success, frame = cameraCapture.read()
    numFramesRemaining -= 1


#Когда нужно использовать мультикам используй grab и retrieve

