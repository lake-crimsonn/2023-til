# pil

- 기본

```python
from PIL import Image

pil_image=Image.open("./learning_python.png")
```

- pil to cv2
- cv2 to pil

```python

numpy_image=np.array(pil_image) # pil 2 cv2
pil_image=Image.fromarray(color_coverted) # cv2 to pil
```
