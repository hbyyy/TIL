

# 1. 아래 문자열의 길이를 구해보세요

q1 = "dk2jd923i1sldxi2ewkskdjfmmvmcmls"

print('1. ', len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해 보세요
#   apple;orange;banana;lemon

print('2. ','apple;orange;banana;lemon')

# 3. 화면에 * 기호 100개를 표시하세요

print('3. ', '*' * 100)

# 4. '30' 을 각각 정수형, 실수형, 복소수형 문자형으로 변환

print('4. ', int('30'))
print('4. ', float('30'))
print('4. ', complex('30'))
print('4. ', str('30'))

# 5. 다음 문자열 'Niceman'에서 'man'문자만 추출해보세요

q5 = 'niceman'
q5_idx = q5.index('man')

print('5. ', q5[q5_idx:q5_idx +3])

# 6. 다음 문자열을 거꾸로 출력 : 'strawberry'

q6 = 'strawberry'
print('6. ', q6[::-1])
print('6. ', list(q6[::-1]))
print('6. ', q6.split())

# 7. 다음 문자열에서 '-'를 제거 후 출력 '010-7777-9999'

q7 = '010-7777-9999'


