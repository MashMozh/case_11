#broken_line это мой#
def main():
    print("Доступные фракталы: ")
    fractals = [square, ice_fractal_1, broken_line ]
    person = int(input("Напишите название желаемого фрактала: "))
    match person:
        case "square":
            size = float(input("Введите размер квадрата: "))
            depth = int(input("Введите глубину рекурсии: "))

            turtle.speed(0)
            square_fractal(size, depth)
            turtle.done()

        case "broken line":
            speed()
            bgcolor("black")
            color("cyan")

            depth = int(input("Введите порядок фрактала: "))
            lenth = int(input("Введите длину начальной линии: "))
            angle = int(input("Введите угол ветвления (например, 30-60): "))

            penup()
            setpos(0, -lenth // 2)
            pendown()
            setheading(90)

            spiral_branch(depth, lenth, angle)
            done()

        case "ice_fractal_1":
            speed()
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

