import random

highest = 10
answer = random.randint(1, highest)
guess = 0

print('please guess a number between 1 and {}: '.format(highest))

while guess != answer:
    guess = int(input())

    if guess == answer:
        print('you got it the first time')
        break
    else:
        if guess < answer:
         print('too low')
         break
        else:
         print('too high')
         break
#
