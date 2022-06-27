mystery = '\U0001f984'

print(mystery)

import unicodedata
print(unicodedata.name(mystery))

print(pop_bytes := mystery.encode('utf-8'))

print(pop_string := pop_bytes.decode('utf-8'))
print(pop_string == mystery)
