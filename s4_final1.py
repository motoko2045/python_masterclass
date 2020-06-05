print('what would you like to work on today? please select from the options: ')
print("""
1:\tlearn python
2:\tlearn mysql
3:\tlearn calculus
4:\tlearn linear algebra
5:\tlearn algorithms
6:\tlearn javascript
7:\tlearn html
8:\tlearn css
9:\tlearn EXIT
""")

while True:
    choice = input()

    if choice == '0':
        break
    elif choice in '123456789':
        print('you chose {}'.format(choice))
        break
