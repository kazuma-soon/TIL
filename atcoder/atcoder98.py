a, b, c, d = [int(x) for x in input().split()]

if a <= c <= b and a <= d <= b:
    print(d - c)
elif c <= a <= d and c <= b <= d:
    print(b - a)
elif   a < c < b:
    print(b - c)
elif c < a < d:
    print(d - a)
else:
    print(0)
    
