choice = "-"
while choice != "0":
    if choice in "123456789":
        print('you chose {}'.format(choice))
        break
    else:
        print("please choose option from below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tLearn JavaScript")
        print("4:\tLearn Ruby")
        print("5:\tLearn PHP")
        print("6:\tLearn Rust")

    choice = input()
