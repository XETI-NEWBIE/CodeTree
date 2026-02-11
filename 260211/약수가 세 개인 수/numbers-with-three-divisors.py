# 약수가 세 개인 수
a, b = list(map(int, input().split()))
total_count = 0

for num in range(a,b+1):
    # 언제나 그렇듯 if문 조건 설정 문제
    # int != iterable => 숫자는 for문에 넣어서 하나씩 꺼낼 수 없음
    # Zerodivisonerror : range는 0부터 시작하기 때문에 0으로 나눌라다가 에러뜬거임
    # num%i ====> 1, num+1 로 수정
    # 해당 숫자(num)의 약수가 몇 개인지 셀 변수 (숫자가 바뀔 때마다 0으로 초기화) 
    divisor_count = 0
    
    for i in range(1, num+1):
        if num%i==0:
            divisor_count += 1 # num/i로 딱 나누어 떨어지면 약수 개수 +1 
        
    if divisor_count == 3:
        total_count+=1
# 들여쓰기 중요
print(total_count)