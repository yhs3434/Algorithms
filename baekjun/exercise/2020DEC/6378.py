def getAnswer(num):
    numStr = str(num)
    val = 0
    for nStr in numStr:
        n = int(nStr)
        val += n
    if val >= 10:
        val = getAnswer(val)
    return val;

while True:
    n = int(input())
    if n == 0:
        break

    val = getAnswer(n)
    print(val)