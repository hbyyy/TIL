# data = list(map(str, input().split()))
# count = 0
#
# for i in range(len(data)):
#     if data.count(data[i-1]) < data.count(data[i]):
# 	    count = i
#
#
# print("{}(이)가 총 {}표로 반장이 되었습니다.".format(data[count], data.count(data[count])))



# 입력
# 원범 원범 혜원 혜원 혜원 유진 유진 혜원
#
# 출력
# 혜원(이)가 총 4표로 반장이 되었습니다.원

import time

vote_dic = {}
vote_max_name = ['NONE']
vote_max = 0
vote = list(input().split())
start = time.time()  # 시작 시간 저장
for i in vote:
    if i in vote_dic:
        vote_dic[i] += 1
    else:
        vote_dic[i] = 1
for i in vote_dic.keys():
    if vote_max < vote_dic[i]:
        vote_max_name.pop()
        vote_max_name.append(i)
        vote_max = vote_dic[i]
    elif vote_max == vote_dic[i]:
        vote_max_name.append(i)
print(vote_max_name, vote_max)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간