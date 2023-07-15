# get-dummies

```python

# 프릭스없이, 프릭스세퍼레이터 없이 super,sub 칼럼 겟더미화
tmp = pd.get_dummies(df[['super','sub']], dtype='uint8', prefix='',prefix_sep='')
tmp

```
