# import argparse
#
# parser = argparse.ArgumentParser()
#
# parser.add_argument(
#     'number',
#     type=int,
#     help='This options stdout number'
# )
# parser.add_argument(
#     '--time',
#     '-t',
#     type=int,
# )
#
# args = parser.parse_args()
#
# print(f'{args.number * args.time}')
# \


def print_test1(str1, str2):
    print(str1)
    print(str2)
    print('this is decorator')
    print(str1)
    print(str2)
    return None


def print_test2(str1, str2):
    print(str1)
    print(str2)
    print('this is decorator')
    print(str1)
    print(str2)
    return None


print_test('asd', 'qwe')
