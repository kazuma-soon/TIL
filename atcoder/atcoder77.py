h, w = [int(x) for x in input().split()]

print('#' * (w + 2))

for i in range(h):
  print('#' + input() + '#')

print('#' * (w + 2))

