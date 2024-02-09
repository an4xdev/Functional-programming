def count_calls_Non_memonized(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls_Non_memonized
def nonMemonizedCatalan(n):
    if n == 0:
        return 1
    else:
        result = 0
        for i in range(n):
            result += nonMemonizedCatalan(i) * nonMemonizedCatalan(n - i - 1)
        return result


n = 10
catalan_10 = nonMemonizedCatalan(n)
print(f"{n}-ta liczba w ciągu Catalana wynosi: {catalan_10}")
print(f"Ilość wywołań funkcji dla n = {n} bez memoizacji: {nonMemonizedCatalan.calls}")