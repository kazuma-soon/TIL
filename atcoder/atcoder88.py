a, b, c, d = [int(x) for x in input().split()]
print(0 if b <= c or d <= a else min(b, d) - max(a, c))