# sorted

- [230704-2-imageGen](/3-deep-learning/7-July/230704-2-imageGen.ipynb)

```python
prob = zip(class_col, list(pred))
prob = sorted(list(prob), key = lambda z: z[1], reverse = True)[:2]
```

---
