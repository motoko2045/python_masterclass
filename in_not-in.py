# ( still on Booleans )

# two use of 'in', here we focus on 'in' as a condition
# 'in' is used in sequences
# *************************
# parrot = 'Norwegian Blue'
# letter = input('Enter a character: ')
#
# if letter in parrot:
#     print('{} is in {}'.format(letter, parrot))
# else:
#     print('I don\'t need that letter')

activity = input('what would you like to do today? ')

if 'cinema' not in activity.casefold:
    print('But I want to go to the cinema')
# string comparisons are case sensitive so we use casefold.
