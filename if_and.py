age = int(input('how old are you?'))

# the following commented out code threw an syntax error

#if age >= 16 and <= 65:
    #print('have a good day at work')

if 16 <= age <= 65:
    print('have a good day at work!')

print('*' * 80)

if age < 16 or age > 65:
    print('enjoy your free time')
else:
    print('have a good day at work :)')
