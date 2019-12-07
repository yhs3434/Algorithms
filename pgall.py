def addOrMul(original, str):
    if (str[0] == "+"):
        return original+int(str[1])
    else:
        return original*int(str[1])

def calculate(x, answer, temp, original, str):
    val = addOrMul(original, str)
    temp2 = temp[:]
    temp2.append(str)
    if(val > x):
        return
    elif(val == x):
        answer.append(temp2)
        return

    calculate(x, answer, temp2, val, "*2")
    calculate(x, answer, temp2, val, "+1")

def makeAnswer(answerArr):
    result = "2"
    flag = False
    for a in answerArr[0]:
        if(a=='*2'):
            if(flag == True):
                result += ")^2"
                flag = False
            else:
                result += "^2"
        elif(a=='+1'):
            flag = True
            result += "*2"
        else:
            print(a)
    return result

def mainFunc(x):
    answer = []
    calculate(x, answer, [], 1, "*2")
    calculate(x, answer, [], 1, "+1")

    minLen = 10000
    answerArr = ['']
    for a in answer:
        if(len(a) < minLen):
            answerArr[0] = a
            minLen = len(a)
    realAnswer = makeAnswer(answerArr)

    result = ""
    for i in range(realAnswer.count(")")):
        result+="("
    result += realAnswer
    realAnswer = result
    print("(2, "+str(x)+") = " + realAnswer)

for x in range(1, 20):
    mainFunc(x)