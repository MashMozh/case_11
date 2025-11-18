import turtle


def ice_fractal(length, depth):
    """
    Рекурсивно рисует ледяной фрактал (кривую Коха).

    Args:
        length (float): длина текущего сегмента
        depth (int): глубина рекурсии
    """
    if depth == 0:
        turtle.forward(length)
        return

    length /= 3

    ice_fractal(length, depth - 1)
    turtle.left(60)

    ice_fractal(length, depth - 1)
    turtle.right(120)

    ice_fractal(length, depth - 1)
    turtle.left(60)

    ice_fractal(length, depth - 1)


def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    length = float(input("Введите длину: "))
    depth = int(input("Введите глубину рекурсии: "))

    ice_fractal(length, depth)

    turtle.done()


if __name__ == "__main__":
    main()
