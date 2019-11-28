# 46
#
# str1 = ''.join([str(x) for x in range(100 +1)])
# sum_number = 0
# for i in str1:
#     sum_number += int(i)
# print(sum_number)



# 47
# people = [
#          ('이호준', '01050442903'),
#          ('이호상', '01051442904'),
#          ('이준호', '01050342904'),
#          ('이호준', '01050442903'),
#          ('이준', '01050412904'),
#          ('이호', '01050443904'),
#          ('이호준', '01050442903'),
#          ]
#
# people_list = set(people)
# print(people_list)

#
# # 49
#
# num_list = list(map(int, input().split()))
# max_num = num_list[0]
# for num in num_list:
#     if max_num < num:
#         max_num = num
# print(max_num)
#
#
# # 50
#
def bubble(n, data):
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    for i in range(n):
        print(data[i], end = " ")

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)