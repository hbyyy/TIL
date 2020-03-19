"""
1018번, 체스판 다시 칠하기

고려할 사항
    1. 검은색 시작? 흰색 시작?
    2. 범위(N + M)
    3. 카운트 방법
"""
N, M = map(int, input().split())
Board = [input() for _ in range(N)]


def check(i, j):
    W = B = 0
    for x in range(8):
        for y in range(8):
            color = Board[i + x][j + y]
            if color == 'W':
                if (x + y) % 2 == 1:
                    W += 1
                else:
                    B += 1
            if color == 'B':
                if (x + y) % 2 == 0:
                    w += 1
                else:
                    B += 1
    return min(W, B)


for i in range(N - 8 + 1):
    for j in range(M - 8 + 1):
        result = check(i, j)
        answer = min(result, answer)

print(answer)
