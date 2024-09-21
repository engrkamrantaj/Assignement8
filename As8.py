def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def multiply(a, b):
    return a*b


def divide(a, b):
    return a/b


x = int(input("Enter first Number = "))
y = int(input("Enter Second Number = "))

z = input("Enter operation(+, -, *, /):")

if z == "+":
    print(add(x, y))

elif z == "-":
    print(subtract(x, y))

elif z == "*":
    print(multiply(x, y))

elif z == "/":
    if y == 0:
        print("infinity")
    else:
        print(divide(x, y))

else:
    print("invalid Input")
