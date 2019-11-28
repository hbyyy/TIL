# 13

planet_list = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']

print(planet_list[int(input())-1])

# 14

while True:
    n = int(input('숫자(0 -> 종료>'))
    if n == 0:
        break
    elif n % 3 == 0:
        print('짝')
    else:
        print(n)

# 15

print(f'안녕하세요. 저는 {input("이름>")}입니다')


# 16

print(input()[::-1])

# 27

students_name_list = input('이름>').split()
students_grade_list = map(int, input('점수>').split())

print({name : grade for name, grade in zip(students_name_list, students_grade_list)})
