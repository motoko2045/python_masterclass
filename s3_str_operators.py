str1 = "he's"
str2 = " probably"
str3 = " pining"
str4 = " for the"
str5 = " fjords"

print(str1 + str2 + str3 + str4 + str5)
print("he's " "probably " "pining " "for the" " fjords")

print("hello " * 5)
print("hello " * (5 + 4)) # without the parens there would be an error
print("hello " * 5 + "4")

today = "friday"

print("day" in today) # true
print("fri" in today) # true
print("thur" in today) # false
print("parrot" in "fjord") # true
