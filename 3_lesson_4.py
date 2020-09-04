def degree(x, y):
    ans = 1
    for i in range(y):
        ans = x * ans
    return ans


print(degree(int(input('Число которое надо возвести в степень: ')), int(input('Cтепень: '))))

