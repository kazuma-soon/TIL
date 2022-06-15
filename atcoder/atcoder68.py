# fibonacci sequence with generater

def fiv(n):
  a, b = 0, 1
  
  for i in range(n):
    yield a
    a, b = b, a + b

# 5番目の値をとる
cnt = 1
for i in fiv(5):
  if cnt == 5:
    print(i)
  cnt += 1