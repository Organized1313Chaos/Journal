
**OpenCV**

- Read the image to numpy array

```
import cv2
import numpy as np

path = r"D:\Home\Github\Journal\Coding\Python3\Image_Processing\CV2\image.jpg"

# Read an image and returns numpy array
img = cv2.imread(path)

# Convert to a NumPy array
img_array = np.array(img)
```

- Display image

```
# Display the image
cv2.imshow("Image", img)

# Wait for the user to close the window
cv2.waitKey(0)
```
    Note:
        - imshow( ImageName, Image): ImageName will be displayed on the window
  
        - waitkey(5000) --> Waits for 5 seconds
        - waitkey() --> Immediately closes the window after opening up
        - waitkey(0) --> Wait for indefinite time
- Convert Image to Grayscale
```
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
```

- Resize the Image
  - `image.shape-->returns dimensions (height, width, rgb value)`
  - Simple resizing
  
    ```
    # Resize the image
    # width: 300, height: 200
    resized_img = cv2.resize(img, (300, 200))

    # Display the resized image
    cv2.imshow("Resized Image", resized_img)
    cv2.waitKey(0)
    ```
  - Preserve aspect ratio
    - interpolation:  
    - `cv2.INTER_AREA --> shrinking`<br>
    - `cv2.INTER_LINEAR --> zooming `
     
        ```
        # Resize the image while preserving aspect ratio

        r = 300.0 / img.shape[1]
        dim = (300, int(img.shape[0] * r))
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Display the resized image
        cv2.imshow("Resized Image", resized_img)
        cv2.waitKey(0)
        ```