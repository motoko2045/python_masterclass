answer = 5

print('please guess number between 1 and 10: ')
guess = int(input())

if guess != answer:
    if guess < answer:
        print('please guess higher')
    else: # guess must be greater than answer
        print('please guess lower')
    guess = int(input())
    if guess == answer:
        print('well done, you guessed it!')
    else:
        print('sorry, you have not guessed correctly')
else:
    print('you got it the first time!')


# altered for nesting if/else
# if guess < answer:
#     print('please guess higher')
#     guess = int(input())
#     if guess == answer:
#         print('well done, you guess it!')
#     else:
#         print('sorry, you have not guessed correctly')
# elif guess > answer:
#     print('please guess lower')
#     guess = int(input())
#     if guess == answer:
#         print('well done, you guess it!')
#     else:
#         print('sorry, you have not guessed correctly')
# else:
#     print('you got it the first time!')
