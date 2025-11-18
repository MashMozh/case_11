import turtle


def square_fractal(size, depth):
    """
    Recursively draws a fractal square.

    Args:
    size (float): side size of the square
    depth (int): recursion depth
    
    Returns:
        None: The function only draws squares.
    """
    
    if depth == 0:
        return

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.forward(size * 0.1)
    turtle.right(10)
    square_fractal(size * 0.9, depth - 1)


def main():
    size = float(input("Введите размер квадрата: "))
    depth = int(input("Введите глубину рекурсии: "))

    turtle.speed(0)
    square_fractal(size, depth)
    turtle.done()


if __name__ == "__main__":
    main()
