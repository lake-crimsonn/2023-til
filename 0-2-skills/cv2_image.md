# cv2_image

```python
### 영역 지정해서 필터 적용하기

import cv2
from glob import glob
top_left_corner, bottom_right_corner = [], []
xy = []

def drawR(event, x, y, flags, params):
    global top_left_corner, bottom_right_corner

    if event == cv2.EVENT_LBUTTONDOWN:
        top_left_corner = [(x,y)]

    elif event == cv2.EVENT_LBUTTONUP:
        bottom_right_corner = [(x,y)]
        cv2.rectangle(img, top_left_corner[0], bottom_right_corner[0], (255,204,255),5)
        cv2.imshow("new",img)

        start = top_left_corner[0]
        end = bottom_right_corner[0]
        roi = img[start[1]:end[1], start[0]:end[0]]
        # roi = img[start[1]-20:end[1]+20, start[0]-20:end[0]]+20

        target = str(start[0])+'_'+str(end[0])

        Number = len(glob('./saveImg/*'))
        cv2.imwrite('./saveImg/'+ target +'.png', roi)
        cv2.imwrite('./saveImg/'+ str(Number) +'.png', roi)
        xy.append([top_left_corner[0],bottom_right_corner[0]])
        print(xy)

img=cv2.imread("./img01.jpg")
cv2.namedWindow("new")
cv2.setMouseCallback("new", drawR)

temp = img.copy()
k = 0
# Close the window when key q is pressed
while k != 113:
# Display the image
    cv2.imshow("new", img)
    k = cv2.waitKey(0)
    # If c is pressed, clear the window, using the dummy image
    if (k == 99):
        image = temp.copy()
        cv2.imshow("new", img)

cv2.destroyAllWindows()

```

---
