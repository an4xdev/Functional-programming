import json
from functools import reduce


with open("data_zad5.json", "r") as file:
    data = json.load(file)


def calculatePercent(el):
    return el["score"] / el["max_possible_score"] * 100


def grade(el):
    g = calculatePercent(el)
    calculated = 0
    if 0 < g <= 50:
        calculated = 2
    elif 51 <= g <= 60:
        calculated = 3
    elif 61 <= g <= 70:
        calculated = 3.5
    elif 71 <= g <= 80:
        calculated = 4
    elif 81 <= g <= 90:
        calculated = 4.5
    else:
        calculated = 5
    return [{"name": el["name"], "surname": el["surname"], "grade": calculated}]


zad5a = list(map(grade, data))

print(zad5a)

print("\n----------------------------------------------------------\n")


def only2(el):
    return el[0]["grade"] < 3


zad5b = list(filter(only2, map(grade, data)))
print(zad5b)

print("\n----------------------------------------------------------\n")


def policz(acc, student):
    full_name = student[0]["name"] + " " + student[0]["surname"]
    if any(full_name in d for d in acc):
        for d in acc:
            d.update((k, v + 1) for k,v in d.items() if k == full_name)
    else:
        acc.append({full_name: 1})
    return acc


zad5c = reduce(policz, zad5b, [])

print(zad5c)
