# Boosting?
![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99E272355D80EDAA2E)
https://bcho.tistory.com/1354
- x를 m1(x)에 넣어서 나온 잘못된 결과의 x를 가중치를 반영해서 다시 m2(x)에 넣는다. 
- 틀린 부분에 가중치를 더하면서 진행한다
- m3(x) 역시 같은 과정을 반복
- y = m1(x) + m2(x) + m3(x) + error3(x)
- 부스팅 기법 알고리즘 -> 그래디언트 부스트
- 그래디언트 부스트 병렬 처리 -> XGboost