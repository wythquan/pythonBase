num = (1, 2, 3, True, "nigga", False, 67)
# num[0] = 5      # error - you cant reassign new values in tuple
# print(num.count(67))
print(len(num))

symb = (1)      # not a tuple cuz it has only one element
print(symb)

symb = (1,)     # it is a tuple cuz it has element and a comma
print(symb)

# for i in num:
#     print(i, end=" ")

# data = 1, 2, 3, True, "nigga"   # this is also a tuple
data = [1, 2, 3, True, "nigga"]
print(tuple(data))

word = "Hello world"
print(tuple(word))
