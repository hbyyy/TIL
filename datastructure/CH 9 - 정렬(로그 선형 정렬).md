# CH 9 - 정렬 (로그 선형 정렬)

> 로그 선형 정렬에는 대표적으로 병합 정렬, 퀵 정렬이 있다.





# 로그 선형 정렬



### 병합 정렬 (merge soet)

- 리스트를 반으로 나누어 정렬되지 않은 리스트를 만든다.
- 나눈 리스트의 크기가 1이 될 때 까지 계속 리스트를 나눈다
- 병합 정렬 알고리즘을 호출하여 리스트를 정렬하고 병합한다.



#### 공간 복잡도

- 배열의 경우 : 제자리에서 정렬되지 않는다
  - O(n)
- 연결 리스트인 경우 : 별도의 저장공간이 필요하지 않다
  - O(logn)



> 데이터가 너무 커서 메모리에 넣지 못한다면 병합 정렬이 좋다. 원래 데이터에서 나눈 하위 데이터 집합이 메모리에 저장할 수 있을 만큼 작아질 때 까지 별도의 파일로 디스크에 저장할 수 있기 때문이다.



#### 구현

```python
# 배열을 나누는 함수
def merge_sort(seq):
    if len(seq) < 2:
        return seq
    
    mid = len(seq) // 2
    
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)

# 나눈 배열을 합친다.
def merge(left, right):
    if not left or not right:
        return left or right
    i, j = 0, 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    
    return result

```





### 퀵 정렬

 퀵 정렬은 리스트에서 기준이 되는 피봇을 하나 고르고, 피벗을 기준으로 피벗보다 큰 값은 오른쪽, 작은 값은 왼쪽으로 옮기는 작업을 한다. 병합 정렬과 비슷하게 리스트의 길이가 1이 될 때까지 분할된 리스트를 만들어 정렬한다.



> 퀵 정렬은 피벗 값을 잘 선택해야 한다. 
>
> 만약 피벗 값을 리스트의 첫번째 원소로 정한다고 하자. 정렬해야 하는 리스트가 역으로 정렬된 리스트라면, 피벗 값을 정하고 원소들을 정리할 때 계속해서 피벗을 뺀 모든 원소들을 피벗의 왼쪽으로 이동시켜야 한다. 즉 한번 실행할 때 1개의 원소씩 정렬이 될 것이다. 이렇게 되면 시간 복잡도는 O(n2)이 되게 되고, 원소가 많다면 스택오버플로우도 발생할 것이다.



#### 구현

```python
def quick_sort(seq):
    if len(seq) < 2:
        return seq
    
    idx = len(seq) // 2
    pivot = seq[idx]
    
    before = list()
    after = list()
    
    for i in range(len(seq)):
        if i == idx:
            continue
        if seq[i] <= pivot:
            before.append(seq[i])
        else:
            after.append(seq[i])
    
    return quick_sort(before) + [pivot] + quick_sort(after)
```

