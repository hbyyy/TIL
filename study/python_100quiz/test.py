# drinks = {
#     'martini' : {'vodka', 'vermouth'},
#     'black russian' : {'vodka', 'kahlua'},
#     'white russian' : {'cream', 'kahlua', 'vodka'},
#     'manhattan' : {'rye', 'vermouth', 'bitters'},
#     'asdadazc' : {'orange juice', 'vodka'}
# }
#
#
# for name, content in drinks.items():
#     if 'vodka' in content and not content & {'cream', 'vermouth'}:
#         print(name)
#
# a = {1, 2}
# b = {2, 3}
#
# print(a|b)


def test_func(a, b):
    print(id(a), id(b))
    print(id(number1), id(number2))
    a = 10
    b = 24
    print(id(a), id(b))


number1 = 1
number2 = 2

test_func(number1,number2)

print(id(number1), id(number2))
print(number1, number2)