N = int(input())
# N+1가 아니라 N번만큼 루프 반복 (임시변수는 _ 처리(횟수만 중요))
for _ in range(N):
    a,b = map(int, input().split())
    # '합' 이므로 카운티 변수 필수
    total_sum=0
    # a부터 b까지 숫자를 하나씩 꺼내준다
    for num in range(a,b+1):
        # 꺼낸 숫자가 짝수라면~
        if  num%2==0:
            total_sum+=num
    
    print(total_sum)   
