s = input().upper()
dic = {}
for i in s:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

mval = 0
for k, v in dic.items():
    if v > mval:
        mval = v

mkey = []
for k, v in dic.items():
    if mval == v:
        mkey += [k]

if len(mkey) > 1:
    print('?')
else:
    print(mkey[0])