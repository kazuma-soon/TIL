a, b, c = (int(x) for x in input().split())
print('YES' if b - a == c - b else 'NO')