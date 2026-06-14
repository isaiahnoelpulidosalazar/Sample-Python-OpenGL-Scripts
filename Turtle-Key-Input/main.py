
import turtle
import random

pixel = 100
colors = ["yellow", "red", "green"]
rd = random.Random()
p = [0, 0, 0]
r = [0, 0, 0]

for a in range(3):
    p[a] = rd.randint(0, 3)

print(f"""
Enter A to start
Enter B to validate your shapes
Enter R to reset the screen
Enter any key to quit
Use the arrow keys for movement

Enter S to draw a Square
Enter T to draw a Triangle
Enter C to draw a Circle

You are required to draw:
- {p[0]} Squares
- {p[1]} Triangles
- {p[2]} Circles
""")

if input("Input: ").capitalize() == "A":
    screen = turtle.Screen()
    screen.title("Sample Python Turtle")
    screen.listen()

    t = turtle.Turtle()
    t.speed(10)


    def move_left():
        t.penup()
        t.setheading(180)
        t.fd(pixel)


    def move_right():
        t.penup()
        t.setheading(0)
        t.fd(pixel)


    def move_up():
        t.penup()
        t.setheading(90)
        t.fd(pixel)


    def move_down():
        t.penup()
        t.setheading(270)
        t.fd(pixel)


    def draw_square():
        t.pendown()
        t.color(colors[rd.randint(0, len(colors) - 1)])
        t.begin_fill()
        for a in range(4):
            t.fd(pixel)
            t.rt(90)
        t.end_fill()
        t.color("black")
        t.penup()
        r[0] += 1
        print(r)


    def draw_triangle():
        t.pendown()
        t.color(colors[rd.randint(0, len(colors) - 1)])
        t.begin_fill()
        for a in range(3):
            t.fd(pixel)
            t.rt(-120)
        t.end_fill()
        t.color("black")
        t.penup()
        r[1] += 1
        print(r)


    def draw_circle():
        t.pendown()
        t.color(colors[rd.randint(0, len(colors) - 1)])
        t.begin_fill()
        t.circle(pixel / 2)
        t.end_fill()
        t.color("black")
        t.penup()
        r[2] += 1
        print(r)


    def validate_shapes():
        c = True
        for a in range(3):
            if r[a] != p[a]:
                c = False
                break
        print("You have completed your goal." if c else "You have not completed your goal.")
        if c:
            exit()


    def reset():
        for a in range(3):
            r[a] = 0
        screen.reset()
        t.speed(10)
        print("Screen reset.")


    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(draw_square, "s")
    screen.onkey(draw_triangle, "t")
    screen.onkey(draw_circle, "c")
    screen.onkey(validate_shapes, "b")
    screen.onkey(reset, "r")
    turtle.done()