import json
from functools import reduce

with open("data_zad4.json", "r") as file:
    data = json.load(file)


def calculateNetto(el):
    return el["quantity_sold"] * el["unit_price"]


print(data[0])
zad4a = list(map(calculateNetto, data))
print(zad4a)


def calculateBrutto(el):
    return calculateNetto(el) + el["tax_rate"] * calculateNetto(el)


zad4b = list(map(calculateBrutto, data))
print(zad4b)


def moreThan80(el):
    return el["quantity_sold"] > 80


zad4c = list(filter(moreThan80, data))
print(zad4c)


def my_sum(a, b):
    return a + b


zad4d = reduce(my_sum, map(calculateBrutto, filter(moreThan80, data)), 0)
print(zad4d)
