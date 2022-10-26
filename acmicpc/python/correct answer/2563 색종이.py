n = int(input())
li = []
for _ in range(n):
    li += [list(map(int, input().split()))]

draws = [[False for _ in range(100)] for _ in range(100)]

for i in range(len(li)):
    x, y = li[i][0], li[i][1]
    for j in range(y-1, y+9):
        for k in range(x-1, x+9):
            draws[j][k] = True

answer = 0
for i in range(100):
    answer += draws[i].count(True)
print(answer)