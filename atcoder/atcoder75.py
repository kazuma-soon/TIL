n, l = [int(x) for x in input().split()]

strings = []
for s in range(0, n):
  strings.append(input())
  
strings.sort()
print(''.join(strings))