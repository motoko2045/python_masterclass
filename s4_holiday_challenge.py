name = input('hello there, what\' your name? ')
print('nice to meet you {}'.format(name))
age = int(input('so how old are you, {}? '.format(name)))
print('thank you, it appears that you\'re ...')

if age >= 18 and age <= 30:
    print('congrats! you qualify to go on holiday')
else:
    if age < 18:
        print('you\'re too young. sorry mate, you can\'t go on holiday.')
    else:
        print('too young for retirement but too old to know better. back to work!')
