from functools import wraps
from itertools import islice
import time

# (a)Napisz dekorator, który konwertuje funkcję zwracającą listę (lub inną kolekcję) na generator.
# Podpowiedź: Wykorzystaj słowo kluczowe yield wewnątrz dekoratora, by zwracać elementy jeden po drugim zamiast całej listy naraz.


def listToGenerator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for i in result:
            yield i
    return wrapper


@listToGenerator
def listOfRange(n):
    return list(range(n))


# print(
#     f"Wybranie 3 liczb z funkcji, która zwraca listę: {list(islice(listOfRange(10),3))}")


# (b)Utwórz dekorator, który umożliwia opóźnioną ewaluację funkcji (tzn. funkcja jest wywoływana dopiero wtedy, gdy jej wynik jest rzeczywiście potrzebny).
# Podpowiedź: Przemyśl, jak możesz wykorzystać domknięcia, aby "zapamiętać" funkcję i jej argumenty, a następnie wywołać ją tylko wtedy, gdy jest to konieczne.

def lazy_evaluation(func):
    def wrapper(*args, **kwargs):
        def delayed_evaluation():
            return func(*args, **kwargs)

        return delayed_evaluation

    return wrapper


@lazy_evaluation
def expensive_computation(x, y):
    return x + y


# print("Przypisanie funkcji do zmiennej")
# result = expensive_computation(3, 5)

# print("Pierwsze wywołanie funkcji: "+str(result()))

# print("Drugie wywołanie funkcji: "+str(result()))

# res = addNumbers(10,5)
# print(f"opóźnione wywołanie funkcji: {res}")
# print(f"opóźnione wywołanie funkcji: {res}")

# (c)Napisz dekorator, który próbuje wywołać funkcję kilkakrotnie (np. w przypadku wystąpienia wyjątku), zanim rzuci błąd.
# Podpowiedź: Użyj pętli oraz obsługi wyjątków. Zastanów się, jak domknięcie może pomóc w zapamiętaniu ilości prób.


def do3Times(func):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        for _ in range(3):
            try:
                func(*args, **kwargs)
                counter += 1
            except:
                pass
        return counter
    return wrapper


@do3Times
def divide(a, b):
    return a//b


# print(f"Próba użycia 3 razy funkcji: {divide(1, 0)}")
# print(f"Próba użycia 3 razy funkcji: {divide(10, 3)}")

# (d)Utwórz dekorator, który transformuje wyjątki rzucane przez funkcję w określony inny wyjątek.
# Podpowiedź: Wykorzystaj blok try i except wewnątrz dekoratora, by przechwytywać wyjątki i rzucić nowy, określony przez Ciebie wyjątek


def changeException(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except:
            raise Exception("Moj tekst w Exception :)")
    return wrapper


@changeException
def parseToInt(number):
    return int(number)


# try:
#     print(f"Próba zamiany '11' na int: {parseToInt('11')}")
# except Exception as e:
#     print(f"Przy próbie zamiany '11' na int został rzucony wyjątek: {e}")

# try:
#     print(f"Próba zamiany 'lol' na int: {parseToInt('lol')}")
# except Exception as e:
#     print(f"Przy próbie zamiany 'lol' na int został rzucony wyjątek: {e}")

# (e)Napisz dekorator, który ogranicza liczbę wywołań danej funkcji w jednostce czasu (rate limiting) - nie więcej jak 3 wykonania w 5 minut.
# Podpowiedź: Pomyśl o wykorzystaniu domknięcia do przechowywania informacji o czasie ostatniego wywołania i ilości wykonanych wywołań. Pamiętaj o funkcjach z modułu time


def rate_limiter(max_calls, period=300):
    calls_times = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal calls_times
            current_time = time.time()
            calls_times = [
                call_time for call_time in calls_times if current_time - call_time < period]

            if len(calls_times) < max_calls:
                calls_times.append(current_time)
                return func(*args, **kwargs)
            else:
                time_to_wait = period - (current_time - calls_times[0])
                raise Exception(
                    f"Rate limit exceeded. Try again in {time_to_wait:.0f} seconds.")

        return wrapper

    return decorator


@rate_limiter(max_calls=3, period=300)  # 3 wywołania w 5 minut
def my_function():
    print("a")


try:
    my_function()
except Exception as e:
    print(e)
try:
    my_function()
except Exception as e:
    print(e)
try:
    my_function()
except Exception as e:
    print(e)
try:
    my_function()
except Exception as e:
    print(e)

# (f)Napisz dekorator, który pozwala na komponowanie kilku dekoratorów w jednym, zachowując odpowiednią kolejność ich wykonywania.
# Podpowiedź: Zastanów się, jak możesz wykorzystać krotki lub listy do przechowywania i wywoływania sekwencji dekoratorów. Wykorzystanie domknięcia może pomóc w zapamiętaniu kolejności.


def compose(*decorators):
    def decorator(func):
        for dec in decorators:
            func = dec(func)
        return func
    return decorator


def memoize_decorator(func):
    memo = {}

    @wraps(func)
    def wrapper(args):
        if args in memo:
            return memo[args]
        result = func(args)
        memo[args] = result
        return result
    return wrapper


def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} wywołana z argumentami: {args}, {kwargs}")
        return result
    return wrapper


def time_based_access(hours_allowed):
    def decorator(func):
        @wraps(func)
        def wrapper(args, **kwargs):
            if not (hours_allowed[0] <= time.localtime().tm_hour < hours_allowed[1]):
                raise Exception("Funkcja niedostępna o tej godzinie.")
            return func(args, **kwargs)
        return wrapper
    return decorator


@compose(
    memoize_decorator,
    logging_decorator,
    time_based_access((9, 10))
)
def my_function(x):
    return x * x


try:
    result = my_function(5)
except Exception as e:
    print(e)
