t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    li = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            li[j] += li[j-1]
    print(li[-1])