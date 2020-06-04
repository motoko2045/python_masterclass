import random

highest = 20
answer = random.randint(1, highest)

print('please guess a number between 1 and {}: '.format(highest))
guess = int(input())

if guess == answer:
    print('you got it!')
else:
    if guess < answer:
        print('please guess higher')
    else:   # guess must be greater than answer
        print('please guess lower')
    guess = int(input())
    if guess == answer:
        print('well done, you guessed it')
    else:
        print('sorry, you have not guessed correctly')
