# dict

- 파이썬 2.7 이전 버전은 딕셔너리가 리스트를 리턴했다.
- 파이썬 3.0 이후부터 dict_keys, dict_values, dict_items객체를 리턴한다.
- 리스트로 변환하지 않더라도 이터레이터를 이용할 수 있다.

```python
a.items()
# dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])
a.values()
# dict_values(['pey', '010-9999-1234', '1118'])

```
