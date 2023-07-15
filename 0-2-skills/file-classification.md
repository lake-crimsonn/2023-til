# 파일분류

```python
from glob import glob
from PIL import Image
import numpy as np
import os
import shutil

base = 'c:/data/transfer-learning/'
fileList = glob(base+'/*.jpg')
for idx, file in enumerate(fileList):
    img = Image.open(file).resize((160,160)).convert('RGB')
    img = np.array(img)
    img = np.reshape(img,(1,160,160,3))
    yhat = model.predict(img)
    predictions = tf.nn.sigmoid(yhat)
    predictions = tf.where(yhat < 0.5, 0, 1)
    pred_name = class_names[predictions[0][0]]
    print(pred_name)

    if not os.path.exists(base+pred_name):
        os.mkdir(base+pred_name)

    newDir = base+pred_name
    newName = pred_name+str(idx+1)+'.jpg'
    os.rename(file, newName)
    shutil.move(base+newName, newDir)
```

- 이름 변경 안 할때

```python
import os
import shutil


SAVE_URL = './saveImg/'
newDir = SAVE_URL+class_name[argmaxNumber]
if not os.path.exists(SAVE_URL+class_name[argmaxNumber]):
    os.mkdir(newDir)
shutil.move(SAVE_URL+newName+'.png', newDir)
```

---
