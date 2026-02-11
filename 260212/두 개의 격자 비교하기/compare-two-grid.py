import sys

# 행(n), 열(m) 입력 받기
n, m = map(int, sys.stdin.readline().split())

# 첫 번째 격자 입력
grid1 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 두 번째 격자 입력
grid2 = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 비교 결과 출력
for i in range(n):
    for j in range(m):
        if grid1[i][j] == grid2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()