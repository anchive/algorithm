n = int(input())
li = list(map(int, input().split()))
mval = max(li)
answer = []

for i in li:
    answer += [i/mval*100]

print(sum(answer)/n)