li = [list(map(int, input().split())) for _ in range(9)]

mval, ival, jval = 0, 1, 1
for i in range(9):
    for j in range(9):
        if li[i][j] > mval:
            mval = li[i][j]
            ival = i+1
            jval = j+1

print(mval)
print(ival, jval)