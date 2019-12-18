def solution(rod):
    length = len(rod)
    cuts = [0 for i in range(length+1)]
    for i in range(length):
        idx = i + 1
        temp = []
        for j in range(1, idx//2+1):
            temp.append(cuts[j]+cuts[idx-j])
        temp.append(rod[i])
        cuts[idx] = max(temp)
    answer = cuts[-1]
    return answer

def memoizedCutRod(p, n):
    r = [-float('inf') for i in range(n+1)]
    return memoizedCutRodAux(p, n, r)

def memoizedCutRodAux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = 0
    if n == 0:
        q = 0
    else:
        q = -float('inf')
        for i in range(1, n+1):
            q = max(q, p[i]+memoizedCutRodAux(p, n-i, r))
    r[n] = q
    return q

print(solution([1,5,8,9,10,17,17,20,24,30,35,36,41,42,44,46,53,67,70,71,71,72]))