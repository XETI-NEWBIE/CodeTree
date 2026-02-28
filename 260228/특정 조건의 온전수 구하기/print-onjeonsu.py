n = int(input())

for i in range(1, n + 1):
    # 조건 1: 2로 나누어 떨어지면 탈락
    if i % 2 == 0:
        continue
    
    # 조건 2: 일의 자리가 5이면 탈락
    if i % 10 == 5:
        continue
    
    # 조건 3: 3의 배수이지만 9의 배수가 아니면 탈락
    if (i % 3 == 0) and (i % 9 != 0):
        continue
        
    # 모든 조건을 통과한 '온전수'만 출력 (공백 포함)
    print(i, end=' ')