s = input()

a = s.index('A')
for i in range(len(s)):
  if s[i] == 'Z':
    z = i
    
print(z - a + 1)


