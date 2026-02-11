import sys

# 4x4 격자 입력 받기
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

total_sum = 0

# 격자를 순회하며 조건에 맞는 원소만 더하기
for i in range(4): # 행 반복
    for j in range(4): # 열 반복
        # 색칠된 칸의 조건: 열 인덱스가 행 인덱스 이하인 경우
        if j <= i:
            total_sum += grid[i][j]

print(total_sum)