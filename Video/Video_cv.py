#Reading and writing

import cv2

videoCapture = cv2.VideoCapture(r"C:\Users\johnw\Pictures\IMG_0384.MOV")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    '1.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),  #YUV encoding
    fps, size)

success, frame = videoCapture.read()
while success: #Loop until no frames
    videoWriter.write(frame)
    success, frame = videoCapture.read()

