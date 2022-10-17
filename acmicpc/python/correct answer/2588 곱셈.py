a = input()
b = input()
answer = 0
for i in range(len(b)-1, -1, -1):
    temp = int(b[i])*int(a)
    answer += temp*(10**(len(b)-i-1))
    print(temp)
print(answer)