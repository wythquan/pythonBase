# file = open("base 1/text8.txt", "a")

# data = input("Enter text:")

# file.write(f"{data}\n")
# # file.write(data + "\n")

# file.close()

file = open("base 1/text8.txt", "r")

data = file.read(5)
# print(data)

for line in file:
    print(line)

file.close()