# Edward Haynes
# 3/19/2025
# P4LAB1
# Turtle graphics program to draw triangle and square


import turtle
win = turtle.Screen()
win.bgcolor("white")
max = turtle.Turtle()

# set the way Max looks
max.pensize(6)
max.pencolor("blue")
max.shape("turtle")



# for loop that runs 4 times
for i in range(4):
    max.forward(100)
    max.right(90)


# while loop that runs 3 times
this_run = 0


while this_run < 3:
    max.forward(100)
    max.left(120)
    this_run += 1





# keeps the window open after the shape is formed
win.mainloop()