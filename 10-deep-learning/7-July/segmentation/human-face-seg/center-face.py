import cv2
import numpy as np

img = cv2.imread('C:\\data\\lapa\\LaPa\\results\\save3.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()