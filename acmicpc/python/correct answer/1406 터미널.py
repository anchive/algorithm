# answer = input()
# commands = [list(map(str, input().split())) for i in range(int(input()))]
# pointer = len(answer)

# for command in commands:
#     if len(command) == 1:
#         order = command[0]
#         if order == "L":
#             if pointer > 0:
#                 pointer -= 1
#         elif order == "D":
#             if pointer < len(answer):
#                 pointer += 1
#         else:
#             if pointer == len(answer):
#                 answer = answer[:pointer-1]
#             elif pointer > 0:
#                 answer = answer[:pointer-1] + answer[pointer:]
#             if pointer > 0:
#                 pointer -= 1
#     else:
#         if pointer == len(answer):
#             answer = answer+command[1]
#         elif pointer == 0:
#             answer = command[1]+answer
#         else:
#             answer = answer[:pointer] + command[1] + answer[pointer:]
#         pointer += 1

# print(answer)

import sys

arr1 = list(sys.stdin.readline().rstrip())
arr2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if arr1:
            arr2.append(arr1.pop())
    elif command[0] == 'D':
        if arr2:
            arr1.append(arr2.pop())
    elif command[0] == 'B':
        if arr1:
            arr1.pop()
    else:
        arr1.append(command[1])

arr1.extend(reversed(arr2))
print(''.join(arr1))