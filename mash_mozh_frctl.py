from turtle import *
import math


def spiral_triangle(order: int, size: float) -> None:
    """
    Draws a recursive spiral triangle fractal.

    Args:
        order (int): Recursion depth.
        size (float): Length of the triangle side.
    """
    
    if order == 0:
        for _ in range(3):
            forward(size)
            left(120)
    else:
        for _ in range(3):
            forward(size)
            left(120)
            penup()
            forward(size / 2)
            right(60)
            pendown()
            spiral_triangle(order - 1, size / 2)
            penup()
            left(60)
            backward(size / 2)
            pendown()


def main() -> None:
    """
    Main function to draw the spiral triangle fractal.
    """
    
    speed()
    bgcolor("black")
    color("orange")

    depth = int(input("Введите глубину рекурсии: "))
    lenth = float(input("Введите длину стороны треугольника: "))

    penup()
    setpos(-lenth / 2, -lenth / (2 * math.sqrt(3)))
    pendown()
    setheading(0)

    spiral_triangle(depth, lenth)
    done()


if __name__ == "__main__":
    main()
    
