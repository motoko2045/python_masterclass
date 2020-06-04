# alternative solution

name = input('hello there, what\'s your name? ')
print('nice to meet you {}'.format(name))

age = int(input('how old are you, {}? '.format(name)))


print('thank you, it appears that you\'re ...')

# change is here to make it more readable
if 18 <= age < 30:
    print('congrats! you qualify to go on holiday')
else:
    if age < 18:
        print('you\'re too young. sorry mate, you can\'t go on holiday.')
    else:
        print('too young for retirement but too old to know better. back to work!')
