low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while True:
    guess = low + (high - low)//2
    highlow = input('my guess is {}. should I guess higher or lower? Enter h or l, or c if my guess was correct'.format(guess)).casefold()

    if highlow == 'h':
        low = guess + 1
    elif highlow == 'l':
        high = guess - 1
    elif highlow == 'c':
        print('I got in in {} guesses!'.format(guess))
        break
    else:
        print('please enter h, l, or c')

    guesses = guesses + 1
