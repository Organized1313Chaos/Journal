# import matplotlib.pyplot as plt
# import PIL

# img = plt.imread(r"D:\ImageProcessing\27_front_doc_1.jpg")
# plt.imshow(im1)
# plt.show()

from PIL import Image
import PIL

img = Image.open(r"D:\ImageProcessing\27_front_doc_1.jpg")
# img.show()

# Case1
# Original Image dimensions are intact
# Rotation not performed properly
# im1 = img.rotate(90)

#Case2
# Add hyperparameters to image
im1 = img.rotate(90, PIL.Image.NEAREST, expand = 1)
# img = plt.imread(r"D:\ImageProcessing\27_front_doc_1.jpg")

# Image Opoens in computer specific applications
# My case: MS Paint
im1.show()
