h, m = map(int, input().split())
m += int(input())

if m >= 60:
    th = m//60
    m = m%60
    if h + th >= 24:
        h = (h+th)%24
    else:
        h += th

print(h, m)