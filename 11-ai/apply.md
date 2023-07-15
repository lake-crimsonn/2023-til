- https://wikidocs.net/46758
```python
    df_잔액시산표['차변잔액'] = df_잔액시산표.apply(lambda x: x['차변합계']-x['대변합계'] if (x['차변합계'] >= x['대변합계']) else 0, axis=1)
```
- x는 df_잔액시산표를 입력변수(매개변수)로 받기
- if문이 True면 '차변잔액'은 '차변합계'-'대변합계'를 적용
- if문이 False면 '차변잔액'에 0을 적용
- axis=1는 열 방향을 칼럼의 연산을 적용