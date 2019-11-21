#  Class

#### 클래스 변수

```python
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
```



위의 예제에서 student_count는 클래스 변수이다. 클래스 변수는 클래스 내부에 선언된 변수로, 인스턴스가 아닌 클래스 전체에 대한 변수이다. 



Student(클래스명)과 student1(인스턴스변수)에 `__dict__`를  출력해보면 아래와 같은 결과값이 나온다

```python
# print(Student.__dict__)
{'__module__': '__main__', '__doc__': '\n    Student class\n    author : Heo\n    Date: 2019.11.21\n    ', 'student_count': 2, '__init__': <function Student.__init__ at 0x7f3a070497a0>, '__str__': <function Student.__str__ at 0x7f3a07049830>, '__repr__': <function Student.__repr__ at 0x7f3a070498c0>, 'detail_info': <function Student.detail_info at 0x7f3a07049950>, '__del__': <function Student.__del__ at 0x7f3a070499e0>, '__dict__': <attribute '__dict__' of 'Student' objects>, '__weakref__': <attribute '__weakref__' of 'Student' objects>}

# print(student1.__dict__)
{'_name': 'Cho', '_number': 2, '_grade': 3, '_details': {'gender': 'male', 'score1': 65, 'score2': 44}, '_email': None}
```



위의 결과값을 자세히 보면, 인스턴스인 student1의 `__dict__`에는 `student_count`  변수가 없다 하지만 ,



```python
print(student1.student_count)
print(student2.student_count)
print(Student.student_count)
```

student1, student2 인스턴스가 존재할 때, 위 구문을 실행하면 결과는 똑같이 `2`  가 나온다.  



이유는 , 인스턴스 네임스페이스에 해당 값이 없다면, 상위에서 검색하기 때문이다. 



#### 인스턴스 메소드, 클래스 메소드,  스태틱 메소드

1. 인스턴스 메소드