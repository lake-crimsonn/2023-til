# save model

```python
import time
t = time.time()

export_path = "./saved_models/{}.h5".format(int(t))
model.save(export_path)

export_path
```

```python
import pandas as pd
from datetime import datetime
timeNow = datetime.now().strftime('%m%d%H%M%S')
export_path = "./csv/{}.csv".format(int(timeNow))

xydf = pd.DataFrame(xy, columns=['top_left_corner','bottom_right_corner'])
xydf.to_csv(export_path)
```

- img save

  ```python
  start = top_left_corner[0]
  end = bottom_right_corner[0]
  roi = img[start[1]:end[1], start[0]:end[0]]
  target = str(start[0])+'_'+str(end[0])

  Number = len(glob('./saveImg/*'))
  cv2.imwrite('./saveImg/'+ target +'.png', roi)
  cv2.imwrite('./saveImg/'+ str(Number) +'.png', roi)
  ```
