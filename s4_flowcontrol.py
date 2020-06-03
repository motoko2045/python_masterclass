# code blocks - indentation based - there is no deliminator such as curly brackets etc.

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i **3))
    # the block is done since the next line is no longer indended
print("*" * 50)
# that's it! like 6 is not a part of the block above it.
