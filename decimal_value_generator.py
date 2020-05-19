from decimal import Decimal


def list_generator():
    list = []
    first = Decimal('2.0')
    last = Decimal('5.5')
    step = Decimal('0.5')
    for i in range(int((last-first)/step)):
        list.append(first + (i * step))
    print(list)


list_generator()