li = [False] * 30

for _ in range(28):
    li[int(input())-1] = True

for i in range(30):
    if li[i] == False:
        print(i+1)