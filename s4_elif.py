name = input("please enter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)
# the code above has a prob. if anything that cannot be
# converted into an integer will make the program crash

if age < 18:
    print('please come back in {0} years'.format(18 - age))
elif age == 900:
    print('sorry, yoda, you die in return of the jedi')
else:
    print('you are old enough to vote')
    print('please put an X in the box')

# python will run line by line, top -> down
# UNLESS you utilize the IF/ELIF/ELSE option to control the flow
# of how python reads the file(program)
