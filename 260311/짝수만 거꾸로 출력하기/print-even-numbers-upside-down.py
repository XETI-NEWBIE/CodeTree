
total_age = 0
count = 0

while True:
    age = int(input())
    
    # 20대가 아니면 (20미만 혹은 30이상이면) 브레이크
    if age < 20 or age >= 30:
        break
        
    total_age += age
    count += 1

# 평균 계산 (첫 번째 사람은 반드시 20대임)
average = total_age / count
print(f"{average:.2f}")