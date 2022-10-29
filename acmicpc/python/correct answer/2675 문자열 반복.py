n = int(input())
for _ in range(n):
    rep, s = input().split()
    answer = ''
    for i in range(len(s)):
        answer += s[i]*int(rep)
    print(answer)