n = input()

count = 0

if int(n) < 100:
    count += int(n)
else:
    count += 99
    for i in range(100, int(n)+1):
        s = str(i)
        if int(s[0])-int(s[1]) == int(s[1])-int(s[2]):
            count += 1

print(count)