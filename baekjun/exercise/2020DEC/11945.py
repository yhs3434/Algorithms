N, M = map(int, input().split())
answer = []
for i in range(N):
    answer.append(input())

for ans in answer:
    print(ans[::-1])