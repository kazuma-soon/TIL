n, m = [int(x) for x in input().split()]

c = []
for k in range(m):
  a, b = [int(x) for x in input().split()]
  c.append(a)
  c.append(b)

for city in range(1, n + 1):
  print(c.count(city))