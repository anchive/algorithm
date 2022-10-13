chess = [1, 1, 2, 2, 2, 8]
temp = list(map(int, input().split()))
print(" ".join([str(chess[i]-temp[i]) for i in range(len(temp))]))