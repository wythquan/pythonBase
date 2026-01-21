# for i in range(10):
#     print(i, end="")

word = "Hello World"

# for i in word[::1]:   # each symbol from first one (index 0)
#     print(i, end="")

# for i in word[1::]:     # each symbol from second one (index 1)
#     print(i, end="")

# for i in word[::-1]:    # each symbol from last one backwards
#     print(i, end="")

# for i in word[4::-1]:   # symbols from 0 to 4 index backwards
#     print(i, end="")

# count = 0
# char = 'l'

# for i in word:
#     if i == char:
#         count += 1

# print(f"There are {count} \'{char}\' symbols")

found = None

for i in "hello":
    if i == 'l':
        found = True
        break
    
# else:
#     found = False
if found != True:
    found = False

print(found)