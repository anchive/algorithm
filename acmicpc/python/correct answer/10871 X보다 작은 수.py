n, x = map(int, input().split())

print(" ".join([str(i) for i in list(map(int, input().split())) if i < x]))