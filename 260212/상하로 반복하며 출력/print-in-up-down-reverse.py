n = int(input())
grid = [[0] * n for _ in range(n)]

for j in range(n):
    if j % 2 == 0:
        # 짝수 번째 열(인덱스 0, 2..): 위에서 아래로 채우기
        num = 1
        for i in range(n):
            grid[i][j] = num
            num += 1
    else:
        # 홀수 번째 열(인덱스 1, 3..): 아래에서 위로 채우기
        num = 1
        for i in range(n - 1, -1, -1):
            grid[i][j] = num
            num += 1

# 최종 격자 출력
for row in grid:
    for val in row:
        print(val, end="")
    print()