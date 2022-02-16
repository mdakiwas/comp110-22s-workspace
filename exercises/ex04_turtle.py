"""This is my third attempt of making turtle art. Please spare me."""

__author__ = "730474304"

from turtle import Turtle, colormode, tracer, update, done
colormode(255)


def main() -> None:  # Makes a abstract sort of turtle art with mountains and planets orbiting a moon.
    """The entrypoint of my scene."""
    tracer(0, 0)  # Disable delay in tracing

    bg_turtle: Turtle = Turtle()
    lump: Turtle = Turtle()
    big_circle: Turtle = Turtle()
    small_circle: Turtle = Turtle()

    background(bg_turtle, -300, -300, 600)
    mountain(lump, -350, -350, 550)        
    moon(big_circle, 200, 70)     
    planet(small_circle, -400, 100)     

    update()  # Now update the rendering
    done()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    


def background(bg_turtle: Turtle, x: int, y: int, box_len: int) -> None:  
    """Makes a solid background."""
    x_coor: int = x
    y_coor: int = y
    length: int = box_len
    bg_turtle.penup()
    bg_turtle.goto(x_coor, y_coor)
    bg_turtle.pendown()

    bg_turtle.pencolor(237, 136, 74)
    bg_turtle.fillcolor(237, 136, 74)
    bg_turtle.begin_fill()
    i = 0
    while i < 4:
        bg_turtle.forward(length)
        bg_turtle.left(90)
        i += 1
    bg_turtle.end_fill()
    bg_turtle.hideturtle()


def mountain(lump: Turtle, x: int, y: int, length: int) -> None:  
    """Makes a triangular structure that's intended to be mountains."""
    x_coor: int = x
    y_coor: int = y
    side_len: int = length
    lump.penup()
    lump.goto(x_coor, y_coor)
    lump.pendown()

    lump_i = 0
    while lump_i < 2:
        pen_fill = [(230, 201, 245), (174, 132, 196), (123, 77, 148), (62, 24, 82), (0, 0, 0)]
        color = 0
        while color < 5:
            lump.pencolor(pen_fill[color])
            lump.fillcolor(pen_fill[color])
            lump.begin_fill()
            i = 0
            while i < 3:
                lump.forward(side_len)
                lump.left(120)
                i += 1
            lump.goto(x_coor, y_coor)
            side_len = side_len - 50
            lump.end_fill()
            color += 1
        lump.penup()
        x_coor = x_coor + 450
        y_coor = y_coor - 30
        lump.goto(x_coor, y_coor)
        lump.pendown()
        lump_i += 1
    lump.hideturtle()


def moon(big_circle: Turtle, x: int, y: int) -> None:  
    """Makes a large circle that's meant to be a moon."""
    x_coor: int = x
    y_coor: int = y

    big_circle.penup()
    big_circle.goto(x_coor, y_coor)
    big_circle.pendown()
    big_circle.pencolor(250, 227, 152)
    big_circle.fillcolor(250, 227, 152)
    big_circle.begin_fill()
    big_circle.circle(150)
    big_circle.end_fill()
    big_circle.hideturtle()


def planet(small_circle: Turtle, x: int, y: int) -> None:  
    """Makes multiple small circles meant to be planets."""
    x_coor: int = x
    y_coor: int = y
    
    small_circle.penup()
    small_circle.goto(x_coor, y_coor)
    small_circle.pendown()

    pen_fill = [(125, 175, 255), (78, 130, 212), (18, 20, 84), (84, 18, 40), (219, 0, 73)]
    
    i = 0
    while i < 5:
        small_circle.pencolor(pen_fill[i])
        small_circle.fillcolor(pen_fill[i])
        small_circle.begin_fill()
        small_circle.circle(75)
        small_circle.end_fill()
        x_coor = x_coor + 200
        y_coor = y_coor - 50
        small_circle.penup()
        small_circle.goto(x_coor, y_coor)
        small_circle.pendown()
        i += 1
    small_circle.hideturtle()


if __name__ == "__main__":
    main()