import cv2
import numpy as np

path = r"C:\Users\johnw\Pictures\ffff.png"

img = cv2.imread(path)
img.itemset((150, 120, 0), 255)
print(img.item(150, 120, 0))


#Установим в определенных пикселях и в определенных канал нужные нам цвета

black_img = np.full((250, 250, 3), 0)

black_img.itemset((200, 200, 0), 255) #B
black_img.itemset((150, 150, 1), 255) #G
black_img.itemset((100, 100, 2), 255) #R

cv2.imwrite('white_test.png', black_img)
print(black_img.shape)

#Slicing

img_no_zero = cv2.imread(path)
img_no_zero[:, :, 1] = 0
cv2.imwrite('no_green.png', img_no_zero)







