# 단어 정렬
# https://www.acmicpc.net/problem/1181

n = int(input())
words = [[] for i in range(51)]
for xxx in range(n):
    word = input()
    if word not in words[len(word)]:
        words[len(word)].append(word)
for word in words:
    word.sort()

for word in words:
    if len(word) > 0:
        for w in word:
            print(w)