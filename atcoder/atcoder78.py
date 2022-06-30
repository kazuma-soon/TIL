import itertools
import collections

n, m = [int(x) for x in input().split()]
l = [input().split() for _ in range(m)]

l = list(itertools.chain.from_iterable(l))
l = collections.Counter(l)

for i in range(1, n + 1):
  num = str(i)
  print(l[num])