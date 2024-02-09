file = open("zad3.txt", "r")
words = file.readline().split(" ")
file.close()

withoutDuplicate = {el for el in words}
withoutDuplicate = list(withoutDuplicate)
withoutDuplicate.sort()
print(withoutDuplicate)

counters = {i: 0 for i in withoutDuplicate}
for el in words:
    count = counters[el]
    count += 1
    counters[el] = count

countersSorted = dict(sorted(counters.items(), reverse=True, key=lambda x: x[1]))
print(countersSorted)


def sortKey(el):
    return len(el[0])


def onlyOne(el):
    return el[1] == 1


longest = list(filter(onlyOne, countersSorted.items()))

longest.sort(key=sortKey, reverse=True)
print(longest[0][0])
