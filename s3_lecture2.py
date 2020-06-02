# escape character portion of lecture

splitString = "this string has been\nsplit over\nseveral\nlines"
print(splitString)
# note the \n for new line between words

tabbedStr = "1\t2\t3\t4\t5"
print(tabbedStr)

# using the escape to use only one type of quote
print('the pet shop owner said "no, no, he\'s uh, ... he\'s resting".')

print("the pet shop owner said \"no, no, he's uh, ... he's resting\".")

print("""the pet shop owner said "no, no, he's uh, ... he's resting". """)
# python knows that everything is a string inside of the triple quotes

# using triple quotes is also how to make one string span multiple lines.
print("""this string has been
split over
several
lines """)

# you can use the back slash to escape the end of the line when using triple quotes
print("""this string has been \
split over \
several \
lines """)

# print("C:\Users\\noname\\notes.txt")
# you have to escape the backslash
# so that it doesnt' think the N in noname isn't a new line

age = 24
print(age)
name= 'charlie'

# you can have multiple arguments for the function print
print('hello ' + name)
print('hello ',name, age) # you cannot concatenate strings and numbers!

# think of values having a type, not a variable because you can reassign
# a variable to a different value of a different type.

print(type(name))
print(type(age))
