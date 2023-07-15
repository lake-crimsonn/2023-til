# dataframe split

```python
df.iloc[:,0].str.split('\\')[1] # index 1
df.iloc[:,0].str.split('\\').str[1] # columns 1
df.iloc[:,0].str.split('\\') # Series to string

df['super'] = df.iloc[:,0].str.split('\\').str[1]
df['sub'] = df.iloc[:,0].str.split('\\').str[2]
df['name'] = df.iloc[:,0].str.split('\\').str[3]
df
```

---
