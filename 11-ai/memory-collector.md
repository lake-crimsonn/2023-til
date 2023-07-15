# 메모리내 변수 제거
```python
all = [var for var in globals() if var[0] != "_"]   # globals() 목록의 첫글자가 _ 로 시작하지 않는 자료의 리스트만 가져와서
for var in all:
    del globals()[var]    # _로 시작하지 않는 모든 자료 삭제함
```