# write a program to print out all the numbers
# from 0 to 20 that aren\'t divisible by 3 or 5

# zed should not appear in output (zed is divisible by everything)

# use the continue statement
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# the same bur without continue
for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
