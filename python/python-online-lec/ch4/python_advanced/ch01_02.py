
# 클래스 변수, 인스턴스 변수


class Student():
    """
    Student class
    author : Heo
    Date: 2019.11.21
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str: {}'.format(self._name)

    def __repr__(self):
        return 'str: {}'.format(self._name)

    def detail_info(self):
        print('Current id : {}'. format(id(self)))
        print('Student Detail info : {} {} {}'.format(
            self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


# self 의미

student1 = Student('Cho', 2, 3, {'gender': 'male', 'score1': 65, 'score2': 44})
student2 = Student('Lee', 4, 1, {'gender': 'Female', 'score1': 85, 'score2': 74})


print(id(student1))
print(id(student2))


print(student1._name == student2._name)
print(student1 is student2)


#dir & __dict__ 확인

print((student1.__dict__))
print((student2.__dict__))

#Docstring

print(Student.__doc__)
print()


student1.detail_info()
student2.detail_info()

Student.detail_info(student1)

print(student1.__class__)

#인스턴스 변수
#직접 접근(PEP문법적으로 권장 X)

print(student1._name, student2._name)
print(student1._email, student2._email)

print()
print()

print(student1.student_count)
print(student2.student_count)
print(Student.student_count)

print()
print()

#공유 확인
print(Student.__dict__)
print()
print(student1.__dict__)
#인스턴스 네임스페이스에 없으면 상위에서 검색
#즉, 도잉ㄹ한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del student2

print(student1.student_count)
print(Student.student_count)
