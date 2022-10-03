import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(i)
        print('visited:',visited)

print(count)