# 38.
# import time
# import random
# score = []
# for i in range(10000):
#     score.append(random.randint(1,100))
# # score = map(int, input().split())
# start = time.time()
# score_sorted = sorted(score)
# last = 0
# result = 0
# cnt = 0
# for i in score_sorted[::-1]:
#     if cnt > 2:
#         break
#     if last != i:
#         last = i
#         cnt += 1
#         result += 1
#     else:
#         result += 1
# print("last :", last, "cnt :", cnt)
# print(result)
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간


grade_list = list(map(int, input().split()))

grade_list.sort(reverse=True)

print(grade_list)

counter = 0

for idx, grade in enumerate(grade_list):
    if idx == len(grade_list - 1grade_list[idx] != grade_list[idx+1]:
        if grade_list[idx] != grade_list[idx + 1]:
            counter += 1
        break
    elif grade_list[idx] != grade_list[idx+1]:
        if grade_list[idx] != grade_list[idx + 1]:
            counter += 1
        break