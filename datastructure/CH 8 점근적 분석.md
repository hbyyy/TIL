# CH 8 점근적 분석



**점근적 분석** 은 어떠한 알고리즘에 큰 데이터 셋을 적용할 때 알고리즘의 제한 동작과 성능을 설명하기 위한 방법이다.

예시로, O(n2)인 정렬 알고리즘으로 10억 개의 데이터 셋을 정렬한다고 해 보자 CPU의 클럭이 1GHz(1초에 10억 개의 명령 수행) 라면 최악의 경우 10억 초가 걸릴 것이다. 이러한 정렬은 n이 커지면 사용할 수 없게 된다.

![](/image/bigocomplexity.gif)

위의 그림과 같이, 데이터가 충분히 많다면 시간복잡도는 다음 순으로 정리된다.

**O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(2^n) < O(n!) **



## P, NP



### P (Polynomial time)

- 결정론적 튜링 기계로 다항시간 안에 풀 수 있는 문제
  - 결정론적 튜링 기계란?
    - 한 계산 단계에 단 하나의 가능한 동작만 있는 튜링 기계



P 문제는 **다항 시간** 안에 풀 수 있다. 즉 어떤 문제를 다항 시간에 풀 수 있다면, 그것은 P 문제이다.



### NP(non-deterministic Polynomial time)

- 비결정론적 튜링 기계로 다항시간 안에 풀 수 있는 문제
  - 비결정론적 튜링 기계란?
    - 각 계산 단계에 여러 가능성을 동시에 고려해야 한다.



## 재귀 알고리즘

### 재귀 알고리즘의 3가지 법칙

1. 재귀 알고리즘은 베이스 케이스가 있어야 한다
   - 재귀 호출을 하지 않고 종료하는 시나리오를 말함
2. 재귀 알고리즘은 상태를 변경하고 베이스 케이스로 돌아간다
3. 재귀적으로 자신을 호출한다



재귀 함수는 각각의 호출에 대해 인수, 반환 주소, 지역 변수를 메모리의 스택 영역에 할당한다. 이렇게 데이터를 넣고 꺼내는 비용, 메모리를 차지하는 비용들이 더해져 재귀 호출은 비용이 많이 들게 된다.

스택 영역이 다 차서 재귀 호출을 더이상 할 수 없다면 스택오버플로우가 발생할 것이다.