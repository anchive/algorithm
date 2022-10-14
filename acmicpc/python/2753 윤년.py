val = int(input())
if val%4 == 0 and val%100 != 0:
    print(1)
elif val%4 == 0 and val%400 == 0:
    print(1)
else:
    print(0)