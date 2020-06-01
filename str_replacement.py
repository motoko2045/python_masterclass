age = 34
print("my age is " + str(age) + " years")
# without the string function, there would be an error

print("my age is {0} years".format(age))
# this works as well, starting with python3

print("there are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
    .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# the format function is inside of the print function

# you can also do it this way
print("there are {0} days in Jan, Mar, May, Jul, Aug, Oct, and Dec"
    .format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
    .format(28, 30, 31))

print("""Jan: {2},
Feb: {0},
Mar: {2},
Apr: {1},
May: {2},
Jun: {1},
Jul: {2},
Aug: {2},
Sep: {1},
Oct: {2},
Nov: {1},
Dec: {2}
""")
