import cv2

clicked = False
pressed = False
def onMouse(event, x, y, flags, param):
    global clicked
    global pressed
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True
    if flags == cv2.EVENT_FLAG_CTRLKEY:
        pressed = True


cameraCapture = cv2.VideoCapture(1)
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('Showing camera feed.Click window or press any key to stop')

success, frame = cameraCapture.read()

while success and cv2.waitKey(1) == -1 and not clicked: #-1 mean no key in pressed ... 27 is ord('Esc')
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyAllWindows('MyWindow')
cameraCapture.release()
