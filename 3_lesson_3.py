def summ(slag_1,slag_2,slag_3):
    if slag_1<slag_2 and slag_1< slag_3:
        return slag_3+slag_2
    elif slag_2<slag_1 and slag_2< slag_3:
        return slag_1+slag_3
    else:
        return slag_1+slag_2
print(summ(int(input('1 слагаемое: ')),int(input('2 слагаемое: ')),int(input('3 слагемое: '))))