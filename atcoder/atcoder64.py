n = int(input())
s = input()

ans = 0
list = [ans]
for i in s:
  ans += 1 if i == 'I' else -1
  list.append(ans)
  
  
print(max(list))