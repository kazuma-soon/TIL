list = [3, 2, 1, 0]

for a in list:
    print(a)

offset = 0

while offset < len(list):
    print(list[offset])
    offset += 1

    
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low!')
    elif number > guess_me:
        print('oops')
        break
    else:
        print('found it!')
        break
    number += 1
    
guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low!')
    elif number > guess_me:
        print('oops')
        break
    else:
        print('found it!')
        break
    number += 1