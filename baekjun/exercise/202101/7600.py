while True:
    inp = input()
    if inp == '#':
        break
    alphabets = set()
    for c in inp:
        if 'a' <= c <= 'z':
            alphabets.add(c)
        elif 'A' <= c <= 'Z':
            c = chr(ord('a') + ord(c) - ord('A'))
            alphabets.add(c)
    print(len(alphabets))