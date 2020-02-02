# 단어 나누기
# https://www.acmicpc.net/problem/1251
# https://github.com/yhs3434/Algorithms

inp = input()
words = []
for i in range(1, len(inp)-1):
    for j in range(i+1, len(inp)):
        word1 = inp[:i]
        word2 = inp[i:j]
        word3 = inp[j:]
        words.append(word1[::-1]+word2[::-1]+word3[::-1])
words.sort()
print(words[0])