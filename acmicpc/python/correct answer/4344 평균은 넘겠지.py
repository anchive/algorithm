n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

for i in li:
    students = i[0]
    ratio = 0
    for j in range(1, len(i)):
        aver = sum(i[1:])/students
        if i[j] > aver:
            ratio += 1
    print(f'{ratio/students*100:.3f}'+'%')