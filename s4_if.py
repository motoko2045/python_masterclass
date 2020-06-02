name = input("please enter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)
# the code above has a prob. if anything that cannot be
# converted into an integer will make the program crash

if age >= 18:
    print('you are old enough to vote')
    print('please put an X in the box')
else:
    print('please come back in {0} years'.format(18 - age))

# do it the other way around ...

if age < 18:
    print('please come back in {0} years'.format(18 - age))
else:
    print('you are old enough to vote')
    print('please put an X in the box')
