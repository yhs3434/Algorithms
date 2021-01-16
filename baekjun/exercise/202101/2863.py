A, B = map(int, input().split())
C, D = map(int, input().split())

val = []
val.append(A/C + B/D)
val.append(C/D + A/B)
val.append(D/B + C/A)
val.append(B/A + D/C)

print(val.index(max(val)))