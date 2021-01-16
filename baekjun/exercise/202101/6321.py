n = int(input())
for i in range(1, n+1):
    print('String #', end='')
    print(i)
    inp = input()
    newStr = ''
    for ch in inp:
        newCh = chr(ord(ch) + 1)
        if newCh == chr(ord('Z') + 1):
            newCh = chr(ord('A'))
        newStr += newCh
    print(newStr)
    print()