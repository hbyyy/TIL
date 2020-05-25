# BFS, DFS

> 이번 포스트에서는 대표적인 그래프 탐색 알고리즘인 BFS(너비 우선 탐색), DFS(깊이 우선 탐색)에 대해 정리할 것이다.





## BFS (너비 우선 탐색)

 BFS는 너비 우선 탐색으로, 해당 노드와 같은 레벨에 있는 노드들을 먼저 순회하는 탐색 알고리즘이다.
![](/image/tree1.png)

 위의 트리에서, BFS라면 0 - 1 - 2 - 3 - 4 - 5 - 6 순으로 순회할 것이다.



### 파이썬으로 그래프 표현

- 파이썬에서는 딕셔너리, 리스트를 이용해 그래프를 표현할 수 있다
- 인접 리스트, 인접 행렬 두 가지 방법이 있다.

![](/image/tree2.png)

```python
# 인접 리스트로 그래프 구현
graph = {'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'G', 'H', 'I'],
        'D':['B', 'E', 'F'],
        'E':['D'],
        'F':['D'],
        'G':['C'],
        'H':['C'],
        'I':['C', 'J'],
        'J':['I']}
```



### BFS 알고리즘 구현

 BFS를 구현하기 위해 큐를 활용한다.

- need_visit 큐와 visited 큐 두개를 사용

```python
def BFS(graph, start_node):
    visited = []
    need_visit = []   
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

# pop(0)은 시간복잡도가 O(n)이니, deque를 사용하면 O(1)의 시간복잡도로 pop을 할 수 있다.

from collections import deque
def BFS2(graph, start_node):
    visited = []
    need_visit = deque()   
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited
```



#### 시간 복잡도

 시간 복잡도는 while문을 보면 된다

위 코드에서, while문은 V + E 번 (노드 수 + 간선 수) 만큼 실행된다. 즉, O(V+E)의 시간복잡도를 가진다.





## DFS(깊이 우선 탐색)

 DFS는 깊이 우선 탐색으로, 해당 노드의 자손 노드들을 먼저 탐색하는 방식이다. 한 노드의 자식을 타고 끝까지 순회한 후, 다시 돌아와서 다른 형제의 자식을 타고 내려가며 순회한다.
![](/image/tree1.png)

 위의 트리에서, BFS라면 0 - 1 - 3 - 4 - 2 - 5 - 6 순으로 순회할 것이다.



### DFS 알고리즘 구현

- BFS와 비슷하지만, DFS는 need_visit **스택**과 visited 큐를 사용한다

![](/image/tree2.png)

```python
def DFS(graph, start_node):
    visited = []
    need_visit = []
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            # 그래프의 왼쪽부터 순회하기 위해 [::-1]로 넣어준다
            # 무향 그래프이므로 중요하지 않지만, 위의 그림에서 보이는 왼쪽 노드들부터 탐색하기 위해서
            need_visit.extend(graph[node][::-1])
    return visited
```



#### 시간 복잡도

 시간 복잡도는 BFS와 동일하게 O(V + E)이다.