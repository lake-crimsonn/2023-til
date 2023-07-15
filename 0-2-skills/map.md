# map

- map(func, iter)

```python
ls = [1,2,3,4,5]
ls[1:3] = list(map(lambda x:x+1,ls[1:3]))
#ls[1],[2]
```

```python
import numpy as np

pred = np.array([0, 1, 0, 1])
pred2 = np.array([0, 1, 0, 1])

def predict(self, X):
    pred = X['Sex'].map({1: 0.0, 0: 1.0}).values.reshape(-1, 1)
    return pred

check_and_print = lambda: print('ok') if not np.array_equal(pred, pred2) else None

check_and_print()  # prints 'ok'
```
```python
df2 = df.copy()
df2['Female'] = list(map(lambda x: 0 if x == 1 else 1, df2['Male']))
df2['No_glasses'] = list(map(lambda x: 0 if x == 1 else 1, df2['Eyeglasses']))
```