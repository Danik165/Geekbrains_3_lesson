def division(*args):
    del_1 = int(input('Делимое: '))
    del_2 = int(input('Делитель: '))
    try:
        return del_1 / del_2
    except ZeroDivisionError or ArithmeticError:
        return "Нельзя делить на 0"


print(division())
