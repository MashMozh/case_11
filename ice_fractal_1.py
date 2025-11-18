from turtle import *


def ice(dpth, size) -> None:
    """
    Draws a recursive ice-like fractal.

    Args:
        dpth (int): The recursion depth.
        size (float): The length of the current segment.
    """
    
    if dpth == 0:
        forward(size)
    else:
        ice(dpth - 1, size / 2)
        left(90)
        ice(dpth - 1, size / 4)
        left(180)
        ice(dpth - 1, size / 4)
        left(90)
        ice(dpth - 1, size / 2)


def main() -> None:
    """
    The main function that reads input values
    and draws the ice fractal.
    """
    
    speed(0)
    bgcolor("black")
    color("cyan")

    depth = int(input("Введите глубину рекурсии: "))
    length = int(input("Введите размер первой линии: "))

    penup()
    setpos(0, 0)
    pendown()
    setheading(0)

    ice(depth, length)
    done()


if __name__ == "__main__":
    main()
