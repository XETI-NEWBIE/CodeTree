
total_sum = 0
count = 0

# while 돌면서 age 인풋
while True:
    age = int(input())
    # 20대가 아니면 반복 종료
    if age < 20 or age >= 30:
        break
    # 합계 / count 더해주기
    total_sum += age
    count += 1

# 평균 계산 및 출력
if count > 0:
    avg = total_sum / count
    print(f"{avg:.2f}")