

arr_1 = [list(map(int, input().split())) for _ in range(3)]
arr_2 = [list(map(int, input().split())) for _ in range(3)]

#  0번 인덱스부터 2번까지 훑기 (range(3)이면 idx는 0,1,2)
for i in range(3):
    for j in range(3):
        # 같은 위치(i, j)의 숫자끼리 곱해서 출력
        print(arr_1[i][j] * arr_2[i][j], end=" ")
    print() # 한 줄 끝날 때마다 줄바꿈
