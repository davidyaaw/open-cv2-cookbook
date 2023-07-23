import cv2

path = r"C:\Users\johnw\Pictures\photo_2022-12-05_12-06-27.jpg"
img = cv2.imread(path)
print(img.shape)

my_roi = img[50:300, 100:400]
img[250:500, 600:900] = my_roi
cv2.imwrite('roi.png',img)
cv2.imwrite('my_roi.png',my_roi)

print(img.shape, img.size, img.dtype)
