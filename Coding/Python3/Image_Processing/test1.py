

import cv2
import pytesseract

# Read image
image = cv2.imread(r"D:\Home\Github\Journal\Coding\Python3\Image_Processing\image.jpg")

# Perform OCR
text = pytesseract.image_to_string(image)

print(text)
