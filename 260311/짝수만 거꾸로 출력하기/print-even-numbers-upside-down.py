
total = 0
cnt = 0

while True:
    n = int(input())
    # 20대 범위 벗어나면 즉시 종료
    if n < 20 or n >= 30:
        break
    
    total += n
    cnt += 1

# 평균 계산
print(f"{total / cnt:.2f}")