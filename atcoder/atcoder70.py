r, g, b = [x for x in input().split()]
print('YES' if int((g + b)) % 4 == 0 else 'NO')