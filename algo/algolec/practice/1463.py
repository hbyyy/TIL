"""
1463. 1로 만들기

1. BFS 사용
    - queue를 이용해 구현
2. DP 사용
    -
"""

from collections import deque
N = int(input())
check = [-1 for _ in range(N +1)]

q = deque()
q.append(N)

while len(q):
    front = q.popleft()
    if front == 1:
        print(check[front])
    if front % 3 == 0: check[front%3]

