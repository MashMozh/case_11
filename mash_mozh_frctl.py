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

    speed()
    bgcolor("black")
    color("cyan")

    depth = int(input("Введите порядок фрактала: "))
    lenth = int(input("Введите длину начальной линии: "))
    angle = int(input("Введите угол ветвления (например, 30-60): "))

    penup()
    setpos(0, -a // 2)
    pendown()
    setheading(90)

    spiral_branch(depth, lenth, angle)
    done()


if __name__ == "__main__":
    main()
  
