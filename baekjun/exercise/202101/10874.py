N = int(input())
students = []
sheet = [((i%5)+1) for i in range(10)]
for _ in range(N):
    arr = list(map(int, input().split()))
    if arr == sheet:
        students.append(_+1)
for student in students:
    print(student)