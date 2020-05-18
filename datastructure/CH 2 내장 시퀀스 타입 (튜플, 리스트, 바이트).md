# CH 2 내장 시퀀스 타입(튜플, 리스트, 바이트)

> 파이썬의 기본 내장 시퀀스 타입에는 문자열, 튜플, 리스트, 바이트, 바이트 배열이 있다
>
> 이번 글에서는 튜플, 리스트, 바이트, 바이트 배열에 대해 정리할 것이다.



## 튜플

- 튜플은 쉼표로 구분된 값으로 이루어진다

```python
t1 = 1, 2
print(t1)
Out : (1, 2)
    
t1[0] = 5
Out : # 튜플은 불변 객체이다.
Traceback (most recent call last)
...
TypeError: 'tuple' object does not support item assignment

# 값이 1개인 튜플을 만드려면, 쉼표를 꼭 붙여줘야 한다.
t2 = (1)
print(type(t2))
Out : <class 'int'>

t2 = (1,) # or t2 = 1,
print(type(t2))
Out : <class 'tuple'>
```



### 튜플 매서드

#### count(), index()

- A.count(x)
  - 튜플 A에 담긴 x 항목의 개수를 반환
- A.index(x)
  - 튜플 A에 있는 첫번째 x 항목의 인덱스를 반환한다.



### 튜플 언패킹

파이썬에서 모든 이터러블한 객체는 **시퀀스 언패킹 연산자 (*)** 로 언패킹 할 수 있다.

```python
x, *y = (1,2,3,4)
print(x)
Out : 1
print(y)
Out : [2,3,4]
```





## 리스트

- 파이썬의 리스트(list) 객체는, **배열**과 유사한 구조이다. 
- 리스트는 크기를 동적으로 조정할 수 있고, 가변 타입이다.



### 리스트 메서드

#### append()

- A.append(x)는 리스트 A 끝에 x 항목을 추가한다.

```python
A = [1, 2, 3]
A.append(2)
print(A)
Out : [1, 2, 3, 2]

#슬라이싱을 이용해도 똑같은 작동을 한다.
A[len(A):] = [1]
print(A)
Out : [1, 2, 3, 2, 1]
```



#### extend()

- A.extend(iterable)은 리스트 A 끝에 이터러블한 객체의 모든 항목을 추가한다.

```python
A = [1, 2, 3]
B = [4, 5]
A.extend(B)
print(A)
Out : [1, 2, 3, 4, 5]

# 슬라이싱 이용
A = [1, 2, 3]
A[len(A):] = B
print(A)
Out : [1, 2, 3, 4, 5]

# 연산자 이용
A = [1, 2, 3]
A += B
print(A)
Out : [1, 2, 3, 4, 5]
```



#### insert()

- A.insert(i, x)는 리스트 A의 i번째 인덱스에 x 항목을 추가한다

```python
A = [1, 2, 3]
A.insert(1, 5)
print(a)
Out : [1, 5, 2, 3]
    
# 슬라이싱 이용
A = [1, 2, 3]
A[1:1] = [5]
print(a)
Out : [1, 5, 2, 3]
```

>  insert() 메서트의 시간 복잡도는 O(n)이다. 리스트의 i 인덱스에 새로운 값을 넣는다면, i 인덱스 뒤의 값은 뒤로 한 칸씩 이동시켜야 하기 때문에 O(n)의 시간복잡도를 가진다.



#### remove(), pop()

-  A.remove(x)는 리스트 A에서 x값을 가진 항목을 삭제한다. x가 존재하지 않으면 ValueError를 일으키고, x가 여러개 존재하면 맨 앞쪽의 원소를 삭제한다
- A.pop(i) 는 리스트 A의 i번째 인덱스 항목을 제거하고, 그 값을 반환한다. i를 지정해주지 않으면 리스트 맨 뒤의 값을 제거하고 반환한다.



#### del 

- 인덱스를 사용하여 특정한 항목을 삭제한다.

```python
A = [1, 2, 3]
del A[0]
print(A)
Out : [2, 3]

# 슬라이싱 사용도 가능
A = [1, 2, 3]
del A[0:2]
print(A)
Out : [3]
    
# 변수 자체를 삭제할 수도 있다
A = [1, 2, 3]
del A
print(A)
Out : 
Traceback (most recent call last)
...
NameError: name 'A' is not defined
```

>  변수를 삭제하고 그 변수가 가리키던 값을 어느 변수도 참조하지 않는다면 파이썬 가비지 컬렉터가 그 데이터를 수집하여 처리해 준다.



#### index(), count()

- A.index(x)는 리스트 A에서 x 항목의 인덱스 값을 반환한다. x값이 없다면 ValueError를 반환한다.

- A.count(x)는 리스트 A에서 x 항목의 갯수를 반환한다.



#### revers()

- A.reverse() 메서드는 리스트 A의 항목들을 반전시킨다.

```python
A = [1, 2, 3]
A.reverse()
print(A)
Out : [3, 2, 1]
    
# 슬라이싱 이용
A = [1, 2, 3]
print(A[::-1])
Out : [3, 2, 1]

```



### 리스트 컴프리헨션

- 파이썬에서 컴프리헨션은 반복되거나 특정 조건을 만족하는 객체를 쉽게 만들어내기 위한 방법이다.
- 리스트 뿐만 아니라 셋, 딕셔너리도 컴프리헨션을 사용할 수 있다

##### 컴프리헨션 형식

- [ 항목 for 항목 in iterable]
- [ 표현식 for 항목 in iterable]
- [ 항목 for 항목 in iterable if 조건]

```python
A = [i for i in range(1, 10)]
print(A)
Out : [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 표현식 이용
A = [i*2 for i in range(1, 10)]
print(A)
Out : [2, 4, 6, 8, 10, 12, 14, 16, 18]

# 조건문 이용
A = [i for i in range(1, 10) if i % 2 == 0]
print(A)
Out : [2, 4, 6, 8]
```

>  컴프리헨션을 이용해 리스트를 만든다면, 짧은 코드로 값이 들어있는 리스트를 만들 수 있다. 코드가 짧으니 좋아 보이지만, 가독성을 위해서는 여러 줄의 반복문과 조건문으로 구현하는게 나을 수도 있다.



## 바이트와 바이트 배열

- 바이트(bytes)와 바이트 배열(bytearray)는 파이썬에서 바이트를 처리하는데 사용할 수 있는 자료형이다
- bytes는 불변 타입으로 문자열 타입과 유사하고, bytearray는 가변 타입으로 리스트 타입과 유사하다.

```python
A = [1, 2, 3]
bytes1 = bytes(A)
print(bytes1)
Out : b'\x01\x02\x03'	# b''는 바이트 문자열이다

# bytes는 불변 객체이다
bytes1[1] = 5
Out :
Traceback (most recent call last)
...
TypeError: 'bytes' object does not support item assignment

bytearray1 = bytearray(A)
print(bytearray1)
Out : bytearray(b'\x01\x02\x03')

#bytearray는 가변 객체이다
bytearray1[1] = 5
print(bytearray1)
Out : bytearray(b'\x01\x05\x03')
```



> 다음 포스트에서는 셋(set)과 딕셔너리같은 컬렉션 자료구조에 대해 정리할 것이다.