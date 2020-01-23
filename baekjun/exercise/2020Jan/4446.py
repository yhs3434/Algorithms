# ROT13
# https://www.acmicpc.net/problem/4446
# https://github.com/yhs3434/Algorithms

vowels = ['a', 'i', 'y', 'e', 'o', 'u']
cons = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

while True:
    try:
        inp = input()
        answer = ''
        for c in inp:
            flag = False
            if ord('A') <= ord(c) <= ord('Z'):
                flag = True
            if ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z'):
                c = c.lower()
                if c in vowels:
                    if not flag:
                        answer += vowels[vowels.index(c)-3]
                    else:
                        answer += vowels[vowels.index(c)-3].upper()
                else:
                    if not flag:
                        answer += cons[cons.index(c)-10]
                    else:
                        answer += cons[cons.index(c)-10].upper()
            else:
                answer += c
        print(answer)
    except:
        break