
# def qsort(num_list):
#     num_list_len = len(num_list)
#     if num_list_len <= 1:
#         return num_list
#     pivot = num_list.pop(num_list_len // 2)
#     num_list_front = []
#     num_list_back = []
#
#     for i in range(num_list_len - 1):
#         if num_list[i] < pivot:
#             num_list_front.append(num_list[i])
#         else:
#             num_list_back.append(num_list[i])
#     return qsort(num_list_front) + qsort(num_list_back)
#
#
# list1 = input().split(' ')
# # 내용을 채워주세요.
#
# print(qsort(list1))

from copy import copy


def qsort1(num_list):
    if len(num_list) <= 1:
        return num_list
    pivot = num_list.pop(len(num_list)//2)
    pivot_front_list = []
    pivot_back_list = []
    for i in range(len(num_list)):
        if num_list[i] < pivot:
            pivot_front_list.append(num_list[i])
        else:
            pivot_back_list.append(num_list[i])

    return qsort1(pivot_front_list) + [pivot] + qsort1(pivot_back_list)


list1 = [9,2]
print(list1)
print(qsort1(list1))
print(list1)

# def qsort2(num_list):
#     if len(num_list) <= 1:
#         return num_list
#     pivot = len(num_list)//2
#     pivot_front_list = []
#     pivot_back_list = []
#     for i in range(len(num_list)):
#         if num_list[i] < num_list[pivot]:
#             pivot_front_list.append(num_list[i])
#         elif num_list[i] > num_list[pivot]:
#             pivot_back_list.append(num_list[i])
#         else:
#             continue
#
#     return qsort2(pivot_front_list) + [num_list[pivot]] + qsort2(pivot_back_list)
#
# list1 = [1,6,9,2,3,4]
# print(list1)
# print(qsort2(list1))
# print(list1)