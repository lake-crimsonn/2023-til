def solution(num1, num2):
    return divmod(num1, num2)[1] # (2,0)

print(solution(8,3))

# 정수를 리턴함
# 8/3 2.6666
# 8//3 2

# 다른풀이
solution = lambda *x: divmod(x[0],x[1])[0]
solution(1,2)

