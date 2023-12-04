import cv2
import os

def find_and_save(imagem_path, output_path):
    image = cv2.imread(imagem_path)
    original = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    thresh = cv2.threshold(blurred, 230, 255, cv2.THRESH_BINARY_INV)[1]

    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    image_number = 0
    for c in contours:
        area = cv2.contourArea(c)



        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
        if 50 <= w <= 3000 and 50 <= h <= 3000:
            ROI = original[y:y + h, x:x + w]
            output_filename = os.path.join(output_path, "photo_{}.jpg".format(image_number))
            
            while os.path.exists(output_filename):
                image_number += 1
                output_filename = os.path.join(output_path, "photo_{}.jpg".format(image_number))

            cv2.imwrite(output_filename, ROI)
            image_number += 1

    cv2.imshow('thresh', thresh)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

input_path = 'input'
output_path = 'output'

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(input_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')): 
        imagem_path = os.path.join(input_path, filename)
        find_and_save(imagem_path, output_path)