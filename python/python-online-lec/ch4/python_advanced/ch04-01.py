# first class function

print(set(dir(iter([1,2,3,4,5]))) - set(dir(range(10))) )

def factorial(n: int) -> int:
    if n == 1:
        return n
    return n * factorial(n-1)


print([*map(factorial, range(1, 6))])
