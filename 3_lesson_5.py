i = input("Введите число: (для окончания '.') ")
z = 0
while i != '.':
    i = i.split(" ")
    a = 0
    while a < len(i):
        try:
            i[a] = int(i[a])
        except ValueError:
            print("Value Error")
            break
        a = a + 1
    for c in i:
        z = z + c
    print(z)
    i = input("Введите число: ")
