shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

for item in shopping_list:
    if item == 'spam':
        break

    print('Buy ' + item)
# output
# Buy milk
# Buy pasta
# Buy eggs

item_to_find = 'spam'
found_at = None

# for index in range(6)
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break # to jump out of a loop

print('item found at position {}'.format(found_at))
