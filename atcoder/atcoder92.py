s = input()
ans = []
for i in range(1, len(s)+1):
    if i % 2 == 1:
        ans.append(s[i-1])

print(''.join(ans))
