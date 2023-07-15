# 오차행렬표

```python
import pandas as pd
from sklearn.metrics import confusion_matrix
conMatrix=confusion_matrix(label_batch, predictions)
conMatrix
```

```python
cnt=len(conMatrix)
pd.DataFrame(conMatrix,
             index=['true_%d' % i for i in range(cnt)],
             columns=['pred_%d' % i for i in range(cnt)] )
```

```python
import seaborn as sns
plt.figure(figsize=(5,3))
sns.heatmap(conMatrix,annot=True, fmt='d',cmap='Blues')
plt.xlabel('predicated label')
plt.ylabel('true label')
```

```python
from sklearn.metrics import classification_report
print(classification_report(label_batch, predictions))
```
