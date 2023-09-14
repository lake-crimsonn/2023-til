from collections import Counter


def solution(k, tangerine):
    answer = 0

    for idx, i in enumerate(Counter(tangerine).most_common()):
        k -= i[1]
        print(k)
        
        if k < 0:
            answer = idx
            return answer
    
    
    return answer

if __name__ == "__main__":
    
    tangerine = [1,3,2,5,4,5,2,3]
    tangerine2 = [1,1,1,1,2,2,2,3]
    k = 6 # 4 2

    print('result:', solution(k, tangerine))