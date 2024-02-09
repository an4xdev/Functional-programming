from functools import lru_cache
import sys
sys.setrecursionlimit(5000)


def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@count_calls
@lru_cache(maxsize=None)
def catalan(n):
    if n == 0:
        return 1
    else:
        result = 0
        for i in range(n):
            result += catalan(i) * catalan(n - i - 1)
        return result


n = 10
catalan_10 = catalan(n)
print(f"{n}-ta liczba w ciągu Catalana wynosi: {catalan_10}")
print(f"Ilość wywołań funkcji dla n = {n} z memoizacją: {catalan.calls}\n")

n = 1000
catalan_1000 = catalan(n)
print(f"{n}-ta liczba w ciągu Catalana wynosi: {catalan_1000}")
