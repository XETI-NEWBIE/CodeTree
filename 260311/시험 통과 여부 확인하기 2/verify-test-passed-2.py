# 학생 수 입력 받기
n = int(input())

# 통과한 학생 수를 셀 변수 초기화
pass_count = 0

# 학생 수만큼 반복 처리하기
for _ in range(n):
    # 4개의 점수를 리스트로 맵핑
    scores = list(map(int, input().split()))
    
    # 4과목의 평균값 구하기
    avg = sum(scores) / 4
    
    # 평균이 60점 이상인지 확인
    if avg >= 60:
        print("pass")
        pass_count += 1  # 통과한 인원 추가해주기
    else:
        print("fail")

# 마지막에 총 통과 학생 수 출력!!!
print(pass_count)
