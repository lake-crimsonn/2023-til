# list에서 dataframe으로 변환

```python
# dataList: 리스트

import pandas as pd
df = pd.DataFrame()
for list in dataList:
    df = pd.concat([df,pd.DataFrame(list)])
df
```

---
