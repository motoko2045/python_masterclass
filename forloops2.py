# we're going to iterate over numbers,
# and append anything that isn't a digit
# to the separators string.

# this lesson did not work. see line 8

number = '9,223;372:036 854,775;807'
separators = ""

for char in number:
    if not char.isnumeric(): # AttributeError: 'str' object has no attribute 'isnumeric'
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
