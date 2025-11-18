import turtle


def draw_branch(length: float):
    """
    Recursively draws a branch:
    1. Draw a line forward.
    2. Make two turns to the right and left.
    3. Reduce the length of the branch.
    4. Stop when the branch is too short.
    Args:
        length (int): First line length.

    Returns:
        None: The function only draws a branches.
    """

    if length < 5:
        return

    turtle.forward(length)

    turtle.right(30)
    draw_branch(length * 0.7)

    turtle.left(60)
    draw_branch(length * 0.7)

    turtle.right(30)
    turtle.backward(length)


def main():
    turtle.speed(0)
    turtle.left(90)
    draw_branch(60)
    turtle.done()


if __name__ == "__main__":
    main()
