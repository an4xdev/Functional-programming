def zad2():
    name = input("Podaj swoje imie: ")
    print(f"Witaj {name}!")


def zad3():
    name = input("Podaj swoje imię: ")
    age = int(input("Podaj ile masz lat: "))
    if age < 0:
        raise Exception("Wiek nie może być ujemny")
    print(f"Witaj {name}!")
    if age < 12:
        print("Dziecko")
    elif 12 <= age < 18:
        print("młodzież")
    else:
        print("dorosły")


def zad4():
    N = int(input("Podaj N, aby obliczyć sumę: "))
    sumOfNumbers = sum(range(N + 1))
    print(f"Suma {N} liczb naturalnych wynosi: {sumOfNumbers}")


def silnia(n):
    if n == 0:
        return 1
    else:
        return silnia(n - 1) * n


def zad5():
    number = int(input("Podaj liczbę naturalną, aby obliczyć silnię: "))
    if number < 0:
        raise Exception("Liczba do silni musi być naturalna")
    print(f"Silnia dla {number} wynosi: {silnia(number)}")


def NWD(a, b):
    while (a % b) != 0:
        mod = a % b
        a = b
        b = mod
    return b


def zad6():
    a = int(input("Podaj 1 liczbę naturalną: "))
    b = int(input("Podaj 2 liczbę naturalną: "))
    if a < 0 or b < 0:
        raise Exception("Liczby powinny być naturalne")
    print(f"NWD liczb: {a} i {b}, wynosi: {NWD(a, b)}")


def reverse(list, index, length):
    if index < length // 2:
        return
    list[index], list[length - index - 1] = list[length - index - 1], list[index]
    reverse(list, index - 1, length)


# zad2()
# zad3()
# zad4()
# zad5()
# zad6()


# list = [1, 2, 3, 4]
# list = list[::-1]
# print(list)

list = list(range(5))
dl = len(list)
reverse(list, dl - 1, dl)
print(list)
