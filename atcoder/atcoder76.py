h, w = [int(x) for x in input().split()]
px = [input() for _ in range(0, h)]

print('#' * (w + 2))

for i in range(0, h):
  print('#' + px[i] + '#')

print('#' * (w + 2))
