a = [chr(x).lower() for x in range(65, 91)]
s = list(input())
t = (set(a) - set(s))
print('None' if t == set() else min(t))