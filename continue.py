shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

for item in shopping_list:
    if item != 'spam':
        print('Buy ' + item)

print('______________________')

# now with the continue keyword

for item in shopping_list:
    if item != 'spam':
        continue

    print('Buy ' + item)
