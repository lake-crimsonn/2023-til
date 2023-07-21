import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
rec = cv2.rectangle(img, (0,372),(512,512), (255,255,255), cv2.FILLED)

cv2.imshow('rec', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img)

cv2.imwrite('C:\\data\\lapa\\LaPa\\results\\mask372.png', img)