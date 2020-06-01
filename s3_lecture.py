# the print function

print('hello world') # print is a function that can print a string literal
print(1 + 2) # it can evaluate arithmetic expressions
print(7 * 6)
print() # this will print an empty line
print('this', 'is more than one', 'argument, each a string.')

print("today is a good day to learn python")
print('python is fun')
print("python's string are easy to use")
print('we can even include "quotes" in strings')
# the above discussed the rules regarding quotes
print("hello" + " world") # this will be concatenated into one string

# we can store strings in variables which makes sense when concatenating
greeting = "hey there "
name = input('please enter your name: ') #"charlie brown"
print(greeting + name)

greet2 = "well hello!"
print(greet2 + " " + name)
# previous example had spaces in strings, here we concatenate a space via empty string
