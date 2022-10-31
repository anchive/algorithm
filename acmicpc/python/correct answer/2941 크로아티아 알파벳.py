cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

answer = ''
counter = 0
while counter+1 <= len(s):
    if counter+3 <= len(s) and s[counter:counter+3] in cro:
        counter += 3
    elif counter+2 <= len(s) and s[counter:counter+2] in cro:
        counter += 2
    else:
        counter += 1
    answer += 'a'

print(len(answer))