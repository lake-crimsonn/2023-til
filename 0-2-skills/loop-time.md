# loop-time

```python
from time import time
loop_time = time()
while(True):
    debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

```

---
