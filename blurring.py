import cv2
img = cv2.imread('FR.png')
blurimg = cv2.blur(img,(500,500))
cv2.imwrite('blurred.png',blurimg)