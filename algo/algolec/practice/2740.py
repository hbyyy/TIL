N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(M)]

x, y, z = len(arr1), len(arr2[0]), len(arr1[0])
answer = [[0 for _ in range(z)] for _ in range(len(arr2))]
for i in range(x):
    for j in range(y):
        for k in range(z):
            answer[i][k] +=