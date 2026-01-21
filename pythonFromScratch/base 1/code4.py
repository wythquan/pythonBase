under = ["koko", "nano"]
nums = [10, 20, 30, 40, 50, True, under, "Hello", 60]     # data type - list. Can include different data types
# print(nums)   # prints list with '[]' and ','

if type(under) == list:   # if 'under' is 'list type
    print("Data:", type(under))
if isinstance(under, list):
    print("Data:", type(under))

# print(type(under))

for i in nums:
    if isinstance(i, list):   # if 'i' is 'list' type
        for q in i:
            print(q, end=" ")
        continue
    print(i, end=" ")

print('\n')

nums = [1, 2, 1, 2, 1, 2, 1, 2]
for i in nums:
    if i == 1:
        index = nums.index(1)
        for q in nums[index::2]:
            print(q, end=" ")
        break

print('\n')

print(len(nums))


print('\n')

temp = [1, 2, 3]
# temp.append(10)
temp.insert(1, 10)
print(temp)

new = [5, 6, 7]

# temp.insert(3, new)
temp.extend(new)
print(temp)


oldTemp = temp.copy()
print("Old temp:", oldTemp)

temp.sort()     # if list.insert(index, otherType) - it would cause a TypeError
                # however if you dont call list.sort(), list.insert(index, otherType) could be done with any type of a vairable
print(temp)

temp.reverse()
print(temp)

print("Old temp:", oldTemp)

# oldTemp.pop()   # deletes the last symbol in list
# oldTemp.pop(index)    # deletes symbol that stands by that index
# oldTemp.remove(value)     # deletes value-symbol from list
oldTemp.pop(1)
print("Old temp:", oldTemp)

# oldTemp.count()           # counts all values that list has
# len(oldTemp)              # same as the one that above
# oldTemp.count(value)      # counts the number of exact value that list has 
