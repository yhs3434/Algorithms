# Java vs C++
# https://www.acmicpc.net/problem/3613
# https://github.com/yhs3434

inp = input()
if inp[0] == '_' or inp[-1] == '_' or ord('A') <= ord(inp[0]) <= ord('Z'):
    print("Error!")
else:
    if inp.count('_') > 0:
        flag = True
        for c in inp:
            if ord('A') <= ord(c) <= ord('Z'):
                flag = False
                break
        if flag:
            arr = inp.split('_')
            if arr.count('') > 0:
                flag = False
                arr.remove('')
            if flag:
                print(arr[0],end='')
                for i in range(1, len(arr)):
                    strr = arr[i]
                    if strr != '':
                        print(strr[0].upper(), end='')
                    print(strr[1:], end='')
            else:
                print("Error!")
        else:
            print("Error!")
    else:
        for c in inp:
            if ord('A') <= ord(c) <= ord('Z'):
                print('_'+c.lower(), end='')
            else:
                print(c, end='')