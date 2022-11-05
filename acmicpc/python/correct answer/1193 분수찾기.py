n = int(input())

num = 0
counter = 0

while counter < n:
    num += 1
    counter += num

gap = counter - n
if num%2 == 0:
    top = num - gap
    bottom = gap + 1
else:
    top = gap + 1
    bottom = num - gap
print(f'{top}/{bottom}')