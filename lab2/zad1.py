def pow(a):
    return a * a


zad1a = [1, 2, 3]


def my_map(func, list):
    new_list = []
    for el in list:
        new_list.append(func(el))
    return new_list


print(my_map(pow, zad1a))


def isEven(a):
    return a % 2 == 0


zad1b = [1, 2, 3, 4, 5, 6]


def my_filter(func, list):
    new_list = []
    for el in list:
        if func(el):
            new_list.append(el)

    return new_list


print(my_filter(isEven, zad1b))


def my_sum(a, b):
    return a + b


zad1c = [1, 2, 3, 4, 5]


def my_reduce(func, list, start=0):
    result = start
    for i in list:
        result = func(result, i)
    return result


print(my_reduce(my_sum, zad1c, 0))
