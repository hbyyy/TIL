def binary_print(n):
    # a = n // 2
    # b = n % 2
    # if a == 0:
    #     return 1
    # return str(binary_print(a)) + str(b)

    return 1 if n // 2 == 0 else str(binary_print(n//2)) + str(n % 2)


print(binary_print(100))



