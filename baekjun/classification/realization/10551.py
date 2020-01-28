# STROJOPIS
# https://www.acmicpc.net/problem/10551
# https://github.com/yhs3434/Algorithms

kb = {
    0: ['1', 'Q', 'A', 'Z'],
    1: ['2', 'W', 'S', 'X'],
    2: ['3', 'E', 'D', 'C'],
    3: ['4', 'R', 'F', 'V', '5', 'T', 'G', 'B'],
    4: ['6', '7', 'Y', 'U', 'H', 'J', 'N', 'M'],
    5: ['8', 'I', 'K', ','],
    6: ['9', 'O', 'L', '.'],
    7: ['0', 'P', ';', '/', '-', '[', "'", '=', ']']
}

cnts = [0] * 8

inp = input()
for c in inp:
    for key in kb:
        if c in kb[key]:
            cnts[key] += 1
            break

for cnt in cnts:
    print(cnt)