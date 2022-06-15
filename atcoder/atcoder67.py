# fibonacci sequence

def fiv(i):
  if i == 0:
    return 0
  if i == 1:
    return 1
  return fiv(i-2) + fiv(i-1)

print(fiv(5))
