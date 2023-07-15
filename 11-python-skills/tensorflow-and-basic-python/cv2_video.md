# cv2 video

```python
import cv2
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while cap.isOpened():

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Done")
        break

cap.release()
cv2.destroyAllWindows()
```

- 다이렉트
- 0은 내장 웹캠

```python
cv2.VideoCapture(cv2.CAP_DSHOW)
```
