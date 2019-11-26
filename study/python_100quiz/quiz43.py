def binary_print(n):
    a = n // 2
    b = n % 2
    if a == 0:
        return 1
    return a + binary_print()

