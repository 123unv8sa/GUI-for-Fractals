import turtle

def main():
    import turtle

    def koch_fract(turtle, divis, size):
        if divis == 0:
            turtle.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
                koch_fract(turtle, divis - 1, size / 3)
                turtle.left(angle)

    divis = 5
    size = 500

    wn = turtle.Screen()
    wn.setup(width=750, height=750)
    wn.bgcolor('black')
    wn.title("Koch fractal")

    turtle.penup()
    turtle.goto(-250, 150)

    turtle.speed(1000000000000000)

    turtle.pendown()
    turtle.pencolor('cyan')

    for i in range(0, 3):
        koch_fract(turtle, divis, size)
        turtle.left(-120)
    
    turtle.hideturtle()
    turtle.Screen()

def stop():
    turtle.bye()