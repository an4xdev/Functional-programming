from functools import reduce
from itertools import islice


def my_map(el):
    reduced = reduce(lambda result, x: result + x**2, el, 0)
    return (len(el), reduced)


def isPrime(el):
    if el < 2:
        return False
    elif el == 2:
        return True
    for n in range(2, el):
        if el % n == 0:
            return False
    return True


def my_filter(el):
    sumDigits = 0
    for i in el:
        temp = i
        while temp > 0:
            sumDigits += temp % 10
            temp = temp // 10
    return isPrime(sumDigits)


def generate_pascals_triangle():
    row = [1]
    while True:
        yield row
        next_row = [1]
        for i in range(1, len(row)):
            next_row.append(row[i - 1] + row[i])
        next_row.append(1)
        row = next_row


pascals_triangle = generate_pascals_triangle()

for _ in range(10):
    foo = next(pascals_triangle)
    mapped = map(my_map, [foo])
    print(list(mapped))


def my_reduce(acc, a):
    print(a)
    acc = acc * sum(a)
    return acc


filtered = islice(filter(my_filter, pascals_triangle), 3)
print(list(filtered))
reduced = reduce(my_reduce, filtered, 1)
print(reduced)
