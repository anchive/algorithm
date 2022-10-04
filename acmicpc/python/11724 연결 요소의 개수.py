import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())

dic = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for _ in range(m):
    a, b = map(int, input().split())
    dic[a] += [b]
    dic[b] += [a]

def dfs(v):
    visited[v] = True
    for i in dic[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

for i in range(1, n+1):
    if visited[i] == False:
        count += 1
        dfs(i)

print(count)