import cv2
import numpy as np

path = r"D:\Home\Github\Journal\Coding\Python3\Image_Processing\CV2\image.jpg"

# Read an image
img = cv2.imread(path)

print(img.shape)
# Display the image
cv2.imshow("Image", img)

# Wait for the user to close the window
cv2.waitKey(-1)

# Resize the image
resized_img = cv2.resize(img, (300, 200))

# Display the resized image
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)

# Resize the image while preserving aspect ratio
r = 300.0 / img.shape[1]
dim = (300, int(img.shape[0] * r))
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Display the resized image
cv2.imshow("Shrinking Image", resized_img)
cv2.waitKey(0)

# Resize the image while preserving aspect ratio
r = 300.0 / img.shape[1]
dim = (300, int(img.shape[0] * r))
resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_LINEAR)

# Display the resized image
cv2.imshow("Shrinking Image", resized_img)
cv2.waitKey(0)

# Image Thresholding


# Perform binary thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Display the thresholded image
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)

