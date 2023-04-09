import turtle

turtle.color('red', 'yellow')
turtle.bgcolor('black')

# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)

# turtle.left(180)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(25)
# turtle.left(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(25)

# turtle.left(180)
# turtle.forward(25)
# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(35)

# num1 = 10
# num2 = 11

# if num1 != num2:
#     print(f'{num1} не равно {num2}')
# elif type(num1) == type(num2):
#     (num1 + num2)
# else:
#     print

# while True:
#     num1 = int(input())
#     num2 = int(input())
#     s = input()

#     if type(num1) == type(num2):
#             if type(s) == str:
#                 if s == "+":
#                     print(num1 + num2)
#                 if s == "-":
#                     print(num1 - num2)
#                 if s == "*":
#                     print(num1 * num2)
#                 if s == "/":
#                     print("/")
#                 if s == "exit":
#                     break

while True:
    s = input('Введіть фігуру:').split(',')

    if s[0] == "square":
        for i in range(4):
            if len(s) > 1:
                turtle.right(int(s[1]))
                if len(s) > 2:
                    turtle.forward(int(s[2]))
            else:
                turtle.right(90)
                turtle.forward(100)
    elif s[0] == "circle":
        for i in range(25):
            turtle.right(15)
            turtle.forward(10)
    else:
        break