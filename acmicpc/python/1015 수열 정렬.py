n = int(input())
li = list(map(int, input().split()))
temp = sorted(li)

for i in range(len(temp)):
    li[li.index(temp[i])] = str(i)

print(" ".join(li))