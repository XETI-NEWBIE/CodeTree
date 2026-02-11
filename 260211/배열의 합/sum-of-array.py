
arr = [list(map(int, input().split())) for _ in range(4)]
count = 0

for row in arr:
    # for cols in row:
        # arr에 첫째줄~ 넷째줄의 각 행의 값들을 합하여 각각 출력한다.
        # arr의 첫 행의 값들을 모두 더하고 ~ 두번째 행의 값들을 모두 더하고 ~ 하는 매우쉬운문제
        # 첫 행 : arr[0]~arr[3] 까지 
    count = sum(row)
    
    print(count)