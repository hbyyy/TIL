# 퀵 정렬(Quick sort)

#### 분할 정복 알고리즘 ( Divide and conqure)

* 어떠한 문제를 작은 문제로 분할하여 해결하는 방법
* 보통 재귀적인 호출을 사용한다.



#### 퀵 정렬



* 분할 정복 알고리즘을 이용한 정렬 방법
* 과정
  1. 리스트 원소 중 하나를 선택(고르는 기준은 상관없다. 주로 중간 원소를 선택)
     * 이 원소를 피봇 이라고 한다.
  2.  리스트를 순회하면서 피봇보다 작은 값은 피봇 앞으로, 피봇보다 큰 값은 피봇 뒤로 이동시킨다. 
  3. 순회를 완료하면 피봇을 기준으로 앞 뒤 리스트를 1번부터 반복한다.
  4. 리스트 길이가 0이나 1이 되면 종료한다.



```python
def qsort1(num_list):
    # 4
    if len(num_list) <= 1:
        return num_list
    # 1
    pivot = num_list.pop(len(num_list)-1)
    pivot_front_list = []
    pivot_back_list = []
    # 2
    for i in range(len(num_list)):
        if num_list[i] < pivot:
            pivot_front_list.append(num_list[i])
        else:
            pivot_back_list.append(num_list[i])
	# 3
    return qsort1(pivot_front_list) 
			+ [pivot] 
			+ qsort1(pivot_back_list)
```

