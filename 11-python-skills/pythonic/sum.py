# *x는 함수들어 오는 인수를 튜플로 패킹
# 익명함수는 이름이 없고 변수에 할당할 수 있다
solution=lambda *x:sum(x)

print(solution(5,2))


# 다른 풀이
def solution(num1:int, num2:int)->int:
    answer = num1 + num2
    return answer

plus = lambda *x: x[0]-x[1]
minus = lambda num1, num2: num1 - num2

print(plus(1,2), minus(2,1)) #-1 1