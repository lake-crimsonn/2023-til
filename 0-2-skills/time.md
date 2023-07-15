```python
import time
start = time.time()
time.time()-start
```

- 현재시간

```python
from time import ctime
import time
timeNow = ctime(time.time())
timeNow
```

- datetime

```python
from datetime import datetime
timeNow = datetime.now()
timeNow = timeNow.strftime('%Y-%m-%d-%H:%M:%S')
timeNow
```
