word = "wythquan goat and best"
# print(word.index('yt'))
word1 = word.split(' ')
# print(word1[1])

for i in range(len(word1)):
    word1[i] = word1[i].capitalize()

print(word1)

result = ", ".join(word1)
print(result)

word = "skateboard"
print(word[5:])

temp = [1, 2, "Skate", False, 3, 4, 5, "nigga", 6, 7, 67]
print(temp[1::2])
