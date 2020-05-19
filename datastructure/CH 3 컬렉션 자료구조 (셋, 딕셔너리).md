# CH 3 컬렉션 자료구조 (셋, 딕셔너리)

> 이번 포스트에서는 컬렉션 자료구조인 셋과 딕셔너리에 대해 정리할 것이다.
>
> 컬렉션 자료구조는 세 가지 속성을 가진다
>
> **멤버십 연산자 : in**, **크기 함수 : len**, **반복성**



## 셋

 **셋**은 반복 가능, 가변적, 중복 요소 없음, 정렬되지 않음 특성을 가진 데이터 타입이다. 주도 **멤버십 테스트**, **중복 제거** 를 할 때 사용한다.



### 셋 메서드

#### add()

A.add(x) 는 셋 A에 x가 없을 경우 x를 추가한다.

```python
s = {"1", "2", "3"}
s.add("4")
print(s)
# 셋은 순서가 없다
Out : {"1", "3", "2", "4"}
```



#### update(), union()

- A.update(B) (A |= B)는  셋 A에 셋 B를 추가한다. 

- A.union(x)(A | B) 은 update와 같지만, 연산 결과를 복사본으로 반환한다.

```python
A = {"1", "2"}
B = {"3", "4"}
# update() 메서드
A.update(B)
print(A)
Out : {'1', '2', '3', '4'}

# union() 메서드
A = {"1", "2"}
C = A.union(B)
print(C)
Out : {'1', '2', '3', '4'}
```



#### intersection(), difference(). clear()

- A.intersection(B)(A&B) 는 A와 B의 교집합의 복사본을 반환한다.

```python
A = {"1", "2"}
B = {"1", "3"}
C = A.intersection(B)
print(C)
Out : {'1'}
```



- A.difference(A-B) 는 A와 B의 차집합의 복사본을 반환한다.

```python
A = {"1", "2"}
B = {"1", "3"}
C = A.difference(B)
print(C)
Out : {'2'}
```



- A.clear()는 A의 모든 항목을 제거한다.

```python
A = {"1", "2"}
A.clear()
print(A)
Out : {}
```



#### discard(), remove()

- A.discard(x)는 A의 항목 x를 제거한다. 반환값은  항상 None 이다.
- A.remove(x)는 discard와 같지만, x가 A에 없을 때 KeyError를 발생시킨다.





## 딕셔너리

딕셔너리는 해시 테이블로 구현되어 있다. 셋과 마찬가지로  반복 가능, 가변적, 중복 요소 없음, 정렬되지 않음 특성을 가지고 **키와 값**으로 매핑된 항목의 컬렉션이다.

> 파이썬 3.7부터는 항목의 삽입 순서를 보존한다.



### 딕셔너리 메서드

#### update(), get()

- A.update(B) 는 딕셔너리 A에 딕셔너리 B를 추가해 준다. 만약 A에 B의 키가 존재한다면, 기존 키의 값을 업데이트

- A.get(key, default=None) 은 딕셔너리 A에서 key의 값을 반환한다. key가 없다면 default 값을 반환한다

```python
A = {1:1, 2:2, 3:3}
print(A.get(1))
Out : 1
print(A.get(5))
Out : None
```



#### pop(), popitem()

- A.pop(key) 는 key 항목을 제거한 후 반환한다.
- A.popitem()은 A에서 한개의 항목을 제거한 후 반환한다.



#### keys(), values(), items()

딕셔너리의 항목을 조회한다. 각각 키, 값, 키와 값을 반환하는데, 주로 반복문에서 사용한다. 



