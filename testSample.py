def solution(answers):
    answer = []

    problemNum = len(answers)
    persons = [[] for i in range(3)]
    for i in range(problemNum):
        persons[0].append((i%5)+1)
        if(i%2==0):
            persons[1].append(2)
        else:
            j=i%8
            if(j==1):
                persons[1].append(1)
            else:
                persons[1].append(j//2+2)
        k=i%10
        if(k==0 or k==1):
            persons[2].append(3)
        if (k == 2 or k == 3):
            persons[2].append(1)
        if (k == 4 or k == 5):
            persons[2].append(2)
        if (k == 6 or k == 7):
            persons[2].append(4)
        if (k == 8 or k == 9):
            persons[2].append(5)
    records = [0, 0, 0]
    for i in range(len(answers)):
        if(answers[i]==persons[0][i]):
            records[0]+=1
        if (answers[i] == persons[1][i]):
            records[1] += 1
        if (answers[i] == persons[2][i]):
            records[2] += 1

    maxScore = max(records)
    for i in range(3):
        if(maxScore == records[i]):
            answer.append(i+1)
    return answer

solution([1,2,3,4,5,1,2,3,4,5])