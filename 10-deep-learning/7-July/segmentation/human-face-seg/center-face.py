import cv2
import numpy as np

img = cv2.imread('C:\\data\\lapa\\LaPa\\results\\test16.png', cv2.IMREAD_UNCHANGED)
img = cv2.resize(img,(198,255))

cv2.imwrite('C:\\data\\lapa\\LaPa\\results\\test17.png',img)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()