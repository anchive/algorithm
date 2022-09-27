N = int(input())
stairs = [int(input()) for _ in range(N)]

answer = []

if N > 2:
    answer.append(stairs[0])
    answer.append(stairs[0] + stairs[1])
    answer.append(max(stairs[0] + stairs[2], stairs[1]+stairs[2]))

    for i in range(3, N):
        answer.append(max(answer[i-2], answer[i-3] + stairs[i-1]) + stairs[i])
    
    print(answer[N-1])
else:
    if N == 1:
        print(stairs[0])
    else:
        print(stairs[0] + stairs[1])