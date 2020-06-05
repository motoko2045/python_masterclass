number = [1, 45, 31, 12, 60]

for n in numbers:
    if n % 8 == 0:
        # reject the list
        print('the numbers are unacceptable')
        break
else: # this else belongs to the for loop, not the if clause
    print('all those numbers are fine')
