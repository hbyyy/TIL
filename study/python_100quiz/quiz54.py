
input_list = list(map(int, input('>>').split()))
input_list.sort()
if input_list[-1] - input_list[0] == len(input_list) -1:
    print('YES')
else:
    print('NO')



#
# stamp = list(int, input().split())
# stamp = sorted(stamp)
# print(stamp)
