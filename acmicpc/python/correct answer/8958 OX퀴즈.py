n = int(input())
li = [input() for _ in range(n)]

for i in li:
    stack = 0
    answer = 0
    for j in i:
        if j == 'O':
            stack += 1
        else:
            stack = 0
        answer += stack
    print(answer)