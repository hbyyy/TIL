from datetime import datetime

# 시간 입력,
month, day = map(int, input('시간 입력(예시: 5월 24일 -> 5 24) >>>').split())
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
target_day = datetime(2020, month, day)

# 1월 1일부터 a월 b일까지 지난 '일'을 계산
count_days = (target_day - datetime(2020, 1, 1)).days
print(target_day - datetime(2020, 1, 1))

print(f'{month}월 {day}일은 /'
      f'{week[(count_days % 7 + 3) if count_days % 7 < 4 else (count_days % 7 - 4)]}'
      f' 요일입니다')


week[(count_days % 7 + 3) if count_days % 7 < 4 else (count_days % 7 - 4)]



# 지난 일을 7로 나눈 나머지를 계산하면 주의 몇번째 날인지 계산할 수 있다.
# 1월 1일이 수요일이므로 수요일이 기준이 됨
# count_days % 7 + 3 if count_days % 7 < 4 else count_days % 7 - 4
# SUN, MON, TUE, WED, THU, FRI, SAT
#  0    1    2    3    4    5    6      <- week 배열의 인덱스
#  4    5    6    0    1    2    3      <- 7로 나눈 나머지


