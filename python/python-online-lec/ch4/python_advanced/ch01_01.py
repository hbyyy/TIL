# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반보 최소화, 메소드

class Student():
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._name, self._number)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._name, self._number)


student1 = Student('Kim', 1, 1, {'gender' : 'Male', 'score1': 95, 'score2' : 82})
student2 = Student('Park', 2, 2, {'gender' : 'Female', 'score1': 77, 'score2' : 92})
student3 = Student('Lee', 3, 3, {'gender' : 'Male', 'score1': 99, 'score2' : 100})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)


students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print()

print(students_list)

result = ', '.join([x._name for x in students_list])
print(f'student name : {result}')

for i in students_list:
    print(repr(i))
    print(i)



    