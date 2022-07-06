def count(p, q):
    return q - p + 1

cnt = 0
for x in range(0, int(input())):
    p, q = [int(i) for i in input().split()]
    cnt += count(p, q)

print(cnt)

