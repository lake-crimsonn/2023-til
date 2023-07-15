# Logisitic Regression

```python
lr_clf = LogisiticRegression(solver='liblinear')
lr_clf.fit(X_train, y_train)
pred = lr_clf.predict(X_test) 
# test로 예측을 하는 이유는 공식이 이미 정해져 있어서
```