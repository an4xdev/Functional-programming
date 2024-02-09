def substractWithTailRecursive(a, b, acc):
    if a < b:
        return (acc,a)
    return substractWithTailRecursive(a-b, b, acc+1)


print(substractWithTailRecursive(16, 3, 0))