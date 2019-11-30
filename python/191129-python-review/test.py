import time


start2 = time.time()
list2 = [i for i in range(10000000)]
print(time.time() - start2)

start1 = time.time()
list1 = [*range(10000000)]
print(time.time() - start1)


def sum1(a : int, b : int) -> int:
    """

    :param a:
    :param b:
    :return:
    """
    return a+b
