from turtle import *


def spiral_branch(order: int, size: float, angle: float) -> None:
    """
    Draws a unique spiral branch fractal recursively.

    Args:
        order (int): The recursion depth.
        size (float): The length of the current branch.
        angle (float): The branching angle in degrees.
    """

    if order == 0:
        forward(size)
    else:
        forward(size / 2)
        left(angle)
        spiral_branch(order - 1, size / 2, angle)
        right(2 * angle)
        spiral_branch(order - 1, size / 2, angle)
        left(angle)
        backward(size / 2)


def main() -> None:
    """
    The main function that reads input values,
    sets up the turtle, and draws the fractal.
    """

    speed(0)
    bgcolor("black")
    color("cyan")

    n = int(input("Введите порядок фрактала: "))
    a = int(input("Введите длину начальной линии: "))
    ang = int(input("Введите угол ветвления (например, 30-60): "))

    penup()
    setpos(0, -a // 2)
    pendown()
    setheading(90)

    spiral_branch(n, a, ang)
    done()


if __name__ == "__main__":
    main()
  
