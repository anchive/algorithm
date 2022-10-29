s = input()
li = [str(-1) for _ in range(26)]

for i in range(97, 123):
    if chr(i) in s:
        li[i-97] = str(s.index(chr(i)))

print(" ".join(li))