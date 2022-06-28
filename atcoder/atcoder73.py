o = input()
olen = len(o)
s = {x for x in o}
slen = len(s)

print('yes' if olen == slen else 'no')