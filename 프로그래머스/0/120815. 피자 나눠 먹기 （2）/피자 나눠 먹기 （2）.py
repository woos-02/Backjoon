def solution(n):
    answer = 0
    for i in range(1, n+1):
        if i*6 % n == 0:
            answer = i
            return answer