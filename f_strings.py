# you cannot concatenate a string and a number
# in comes f strings (you don't have to use the format function)

greeting = "oy!"
age = 23
name = "charlie"
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}") # extra formatting
# no variable name, we just used an expression
pi = 22 / 7
print(f"Pi is approximately {pi}")
