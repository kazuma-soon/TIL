odd  = input()
even = input()

pw = []
for o, e in zip(odd, even):
  pw.append(o)
  pw.append(e)
  
if len(odd) > len(even):
  pw.append(odd[-1])

print(''.join(pw))