# star_num = int(input())
#
# star = '*'
# star_num_list = ['*' * (2*x - 1) for x in range(1, star_num + 1)]
# for line in range(star_num):
#     print('{:^100}'.format(star_num_list[line]))
#
#
#
#

star_num = int(input())
for i in range(1, star_num + 1):
    print(' ' * (star_num-i) + ('*' * (2*i - 1)))

