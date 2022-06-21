from pprint import pprint
import collections as co

plain = {'a': 1, 'b': 2, 'c': 3}
fancy = co.OrderedDict({'a': 1, 'b': 2, 'c': 3})

pprint(plain)
print()
pprint(fancy)
