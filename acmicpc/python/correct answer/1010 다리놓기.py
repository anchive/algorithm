T = int(input())

def factorial(n):
    value = 1
    for i in range(1, n+1):
        value *= i
    return value

for _ in range(T):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    print(factorial(b) // (factorial(a) * factorial(b-a)))