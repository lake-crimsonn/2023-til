# train, val, test셋으로 나누기

```python
from sklearn.model_selection import train_test_split

# test_size 명시하지 않으면 0.25
train, test = train_test_split(df3, random_state=777)
train, validation = train_test_split(train, random_state=777)

# 인덱스 초기화
train.reset_index(inplace=True, drop=True)
validation.reset_index(inplace=True, drop=True)
test.reset_index(inplace=True, drop=True)

# 저장
train.to_csv('c:/data/kfood2/train.csv', header=False)
test.to_csv('c:/data/kfood2/test.csv', header=False)
validation.to_csv('c:/data/kfood2/valid.csv', header=False)
```
