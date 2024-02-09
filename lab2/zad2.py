strings = ["angielski", "rosyjski", "niemiecki", "chiński", "japoński", "włoski"]

print(sorted(strings))
strings = ["angielski", "rosyjski", "niemiecki", "chiński", "japoński", "włoski"]


def length(el):
    return len(el)


strings.sort(reverse=True, key=length)
print(strings)

strings = ["angielski", "rosyjski", "niemiecki", "chiński", "japoński", "włoski"]


# c) według ilości samogłosek w napisach
def samogloski(el):
    count = 0
    for i in el:
        if "a" == i or "e" == i or "u" == i or "i" == i or "y" == i:
            count += 1
    return count


strings.sort(key=samogloski)
print(strings)

strings = ["angielski", "rosyjski", "niemiecki", "chiński", "japoński", "włoski"]


def unique(el):
    return {i for i in el}


strings.sort(key=unique)
print(strings)

strings = ["angielski", "rosyjski", "niemiecki", "chiński", "japoński", "włoski"]


def letterA(el):
    return "a" in el


strings.sort(key=letterA, reverse=True)
print(strings)
