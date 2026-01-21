# try:
#     x = input("enter DIGIT: ")
#     x += 5
#     print(x)
# except TypeError:
#     print("You didnt entered digit.")

# try:
#     x = int(input("enter DIGIT: "))
#     x += 5
#     print(x)
# except ValueError:
#     print("You didnt entered digit.")


try:
    x = int(input("enter digit"))
    y = int(input("enter second digit"))
    res = x/y
except ZeroDivisionError:
    print("Division by zero is impossible")
else:           # works when try is correct without erorrs
    print("else")
finally:        # works always after try or except
    print("finally")