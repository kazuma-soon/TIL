a, b, c, d = [int(x) for x in input().split()]
if (a <= c) & (c <= b <= d):
  print(b - c)
elif (c <= a <= d) & (d <= b):
  print(d - a)
elif (a < c < b) & (a < d < b):
  print(d - c)
elif (c < a < d) & (c < b < d):
  print(b - a)
else:
  print(0)
  