# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

s = input()
i = 0
alphabets = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz']
chars = []
while i<len(s):
    if i+1<len(s):
        if s[i:i+2] in alphabets:
            if i+2<len(s):
                if s[i:i+3]=='dz=':
                    chars.append(s[i:i+3])
                    i+=3
                else:
                    if s[i:i+2] == 'dz':
                        chars.append(s[i:i+1])
                        i+=1
                    else:
                        chars.append(s[i:i + 2])
                        i+=2
            else:
                if s[i:i+2] == 'dz':
                    chars.append(s[i:i+1])
                    i += 1
                else:
                    chars.append(s[i:i + 2])
                    i += 2
        else:
            chars.append(s[i:i + 1])
            i+=1
    else:
        chars.append(s[i:i + 1])
        i+=1
print(len(chars))

