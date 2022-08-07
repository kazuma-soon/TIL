n, k = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
print(sum(sorted(l)[-k:]))


