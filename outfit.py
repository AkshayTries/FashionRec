import urllib.request
import cv2
import numpy as np

# Load the image
urllib.request.urlretrieve("http://s3-eu-west-1.amazonaws.com/we-attributes/dress/35/808d0bf9fe9745fca13ab461f86e0e4e.jpg.png", "D:\database\outfit0.jpg")
image_path = "D:\database\outfit0.jpg"
image = cv2.imread(image_path)
"""
Now let's try with `cv2.CHAIN_APPROX_SIMPLE`
"""
#img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

 
# B, G, R channel splitting
blue, green, red = cv2.split(image)
 
# detect contours using blue channel and without thresholding
contours1, hierarchy1 = cv2.findContours(image=blue, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
#print(contours1)
contours1=contours1[1:]
larg_con=max(contours1,key=cv2.contourArea)
print(larg_con)
x,y,w,h = cv2.boundingRect(larg_con)
cropped=image[x:x+h,y:y+w]
cv2.imwrite("cropped.jpg",cropped)
# draw contours on the original image
image_contour_blue = image.copy()
cv2.drawContours(image=image_contour_blue, contours=contours1, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
# see the results
cv2.imshow('Contour detection using blue channels only', image_contour_blue)
cv2.waitKey(0)
cv2.imwrite('blue_channel.jpg', image_contour_blue)
cv2.destroyAllWindows()
 
#-------------------------------------------------------------
# Load the image
'''image = cv2.imread(image_path)

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection
edges = cv2.Canny(blur, 50, 150)

# Perform morphological operations to close gaps in between object edges
kernel = np.ones((5, 5), np.uint8)
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Find contours of objects
contours, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the largest contour (assuming it's the person)
largest_contour = max(contours, key=cv2.contourArea)

# Create a mask for the person
person_mask = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.drawContours(person_mask, [largest_contour], -1, (255), -1)

# Invert the mask to keep the outfit
outfit_mask = cv2.bitwise_not(person_mask)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=outfit_mask)
result_path = 'result.jpg'
cv2.imwrite(result_path, result)
# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
