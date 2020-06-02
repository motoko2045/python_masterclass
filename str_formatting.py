for i in range(1,13):
    print("no. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
print()

for i in range(1,13):
    print("no. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
print() # the second digit is how many spaces

for i in range(1,13):
    print("no. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))
print() # the less than symbol will align to the left

for i in range(1,13):
    print("no. {0:2} squared is {1:>3} and cubed is {2:>4}".format(i, i**2, i**3))
print() # greater than, aligning to the right

for i in range(1,13):
    print("no. {0:2} squared is {1:3} and cubed is {2:^4}".format(i, i**2, i**3))
print() # carrot centers things

for i in range(1,13):
    print("no. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
print() # 4 is the field width

print("Pi is approximately {0:12}".format(22/7))
# general format that defaults to printing 15 decimals

print("Pi is approximately {0:12f}".format(22/7))
# specifying a floating decimal point number with the 'f'

print("Pi is approximately {0:12.50f}".format(22/7))
# still specifying a floating point format ('f') and with
# the precision of 50. 50 points after the decimal point

print("Pi is approximately {0:52.50f}".format(22/7))
# this and all after are specifying a field width of 50

print("Pi is approximately {0:62.50f}".format(22/7))

print("Pi is approximately {0:62.50f}".format(22/7))

print("Pi is approximately {0:<72.50f}".format(22/7))

print("Pi is approximately {0:<72.54f}".format(22/7))
