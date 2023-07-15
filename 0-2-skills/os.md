# os

- [참고 링크](https://engineer-mole.tistory.com/68)

```python
import os

os.chdir('c:/data/')
os.getcwd()
os.listdir()
os.mkdir(base+pred_name)

os.path.splitext(filename)[1] # '.txt'
os.path.splitext(filename)[0] # '파일명'

print("join(): " + os.path.join(os.getcwd(), "file.py"))
print(os.path.join("dirA", "dirB", "/dirC")) # 슬래시를 루트로 보는 경향이 있다.

print("join(): " + os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.py"))
# __file__ 실행중인 파일 표시
# os.path.abspat 절대경로로 변환

path_to_zip # 'C:\\Users\\user\\.keras\\datasets\\cats_and_dogs.zip'
os.path.dirname(path_to_zip) # 'C:\\Users\\user\\.keras\\datasets'
```

---
