# 약수의 합
# https://programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    answer = 0
    if(n==0):
        return 0
    aliquots = []
    for i in range(1, int(n**(1/2)+1)):
        if (n%i==0 and i not in aliquots):
            aliquots.extend(list(set([i, n//i])))
    answer = sum(aliquots)
    return answer

print(solution(3000))
print(solution(5))