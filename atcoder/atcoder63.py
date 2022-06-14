n = int(input())
s = list(input())

list = []
ans = 0
for i in s:
  if i == 'I':
    list.append(ans := ans + 1)
  else:
    list.append(ans := ans - 1)
  
print(max(list) if max(list) >= 0 else 0)