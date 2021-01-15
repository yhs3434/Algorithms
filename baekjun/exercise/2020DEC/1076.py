val = 0
resistTable = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

inp1 = input()
inp2 = input()
inp3 = input()

num1 = resistTable[inp1]
num2 = resistTable[inp2]
num3 = 10 ** resistTable[inp3]

val = int(str(num1) + str(num2)) * num3
print(val)