import cv2
import numpy as np
import matplotlib.pyplot as plot

img = cv2.imread('C:/Users/win/Desktop/image_processing/a.jpg',1)
edges = cv2.Canny(img,400,400)


cv2.imshow('image1',img)
cv2.imshow('image2',edges)


cv2.waitKey(0)
cv2.destroyAllWindows()