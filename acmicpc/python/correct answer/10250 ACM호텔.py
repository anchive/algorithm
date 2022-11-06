n = int(input())
for _ in range(n):
    h, w, n = map(int, input().split())
    if n%h == 0:
        floor = h
        room = n//h
    else:
        floor = n%h
        room = n//h+1
    if room < 10:
        print(f'{floor}0{room}')
    else:
        print(f'{floor}{room}')