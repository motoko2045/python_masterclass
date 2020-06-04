# start / stop / step values - just like slicing
# you can also use negative too like in slices

for i in range(0, 10, 2):
    print('i is now {}'.format(i))

# once again, using range
age = int(input('how old are you? '))

if age in range(16, 66):
    print('work, work, work')
else:
    print('too young to know better - too old to care')
