import cv2

image = cv2.imread('input/test_image.jpg')

height, width, _ = image.shape

percentage_width = 0.5
percentage_height = 0.5

x = 0
y = 0
crop_width = int(width * percentage_width) 
crop_height = int(height * percentage_height)

cv2.rectangle(image, (x, y), (x + crop_width, y + crop_height), (0, 255, 0), 2)

cv2.imshow('Image with Contour', image)
cv2.waitKey(0)

cropped_image = image[y:y+crop_height, x:x+crop_width]

cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()