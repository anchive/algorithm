dices = list(map(int, input().split()))

if len(set(dices)) == 1:
    print(10000 + dices[0] * 1000)
elif len(set(dices)) == 2:
    if dices.count(dices[0]) == 2:
        print(1000 + dices[0] * 100)
    elif dices.count(dices[1]) == 2:
        print(1000 + dices[1] * 100)
else:
    print(max(dices) * 100)