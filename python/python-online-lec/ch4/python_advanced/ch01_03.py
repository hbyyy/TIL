# chapter 01-3
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스태틱 메소드



class Student:
    """
    Student class
    Author : HBY
    Date : 191121
    
    """


    #Class variable
    tuition = 1.0
    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def detail_info(self):
        return 'Student Detail Info : {}, {}, {}, {}, {}, {}'.format(self._id, self.full_name(), self._email, self._grade, self._tuition, self._gpa)

    def get_fee(self):
        return 'Before tuition -> ID : {}, Fee : {}'.format(self._id, self._tuition)

    def get_fee_culc(self):
        return 'After tuition -> ID : {}, Fee : {}'.format(self._id, self._tuition * Student.tuition)




student1 = Student(1, 'Kim', 'sarang', 'llaos@naver.com', '2', 400, 3.5)
