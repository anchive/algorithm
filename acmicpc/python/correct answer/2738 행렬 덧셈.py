n, m = map(int, input().split())
li = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(2):
    for i in range(n):
        val = list(map(int, input().split()))
        for j in range(len(val)):
            li[i][j] = str(int(li[i][j]) + val[j])

for i in li:
    print(" ".join(i))