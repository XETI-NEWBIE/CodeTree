
# 배열의 값을 3배로 !

arr = [list(map(int, input().split())) for _ in range(3)]
# arr = int(input)
rows = 3
cols = 3

for i in range(rows):
    for j in range(cols):
        print(arr[i][j]*3, end=" ")
    print()