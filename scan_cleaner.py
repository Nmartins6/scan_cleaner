import cv2

image = cv2.imread('image_path.jpg')

x, y, width, height = 0, 0, 1150, 1700

cropped_image = image[y:y+height, x:x+width]

cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()