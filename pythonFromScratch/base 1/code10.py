# try:
#     file = open("file.txt", "r")
# except FileNotFoundError:
#     print("file with this name doesnt exist")
# else:
#     print(file.read())
# finally:
#     file.close()


try:
    with open("base 1/file.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("file with this name doesnt exist")