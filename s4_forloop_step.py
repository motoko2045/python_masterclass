# write a program to print out all the numbers from 0 to 100
# that are divisible by 7
# zero is considered to be divisible by all other integers,
# so your output should include zero

for i in range(0, 101, 7): # using the step value in range
    print(i)


for i in range(101)[::7]: # iterating 0 through 101 using step via slice
    print(i)
