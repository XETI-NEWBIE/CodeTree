n = int(input())

for i in range(n):
    if i % 2 == 0:
        # 정방향 출력: 1, 2, ..., n
        for j in range(1, n + 1):
            print(j, end="")
    else:
        # 역방향 출력: n, n-1, ..., 1
        for j in range(n, 0, -1):
            print(j, end="")
    print() # 줄바꿈