
clinic_counts = [0, 0, 0, 0]

# 3명의 정보를 순서대로 입력받아 처리
for _ in range(3):
    info = input().split()
    symptoms = info[0]      
    temperature = int(info[1]) 
    
    # 분류 규칙 적용
    if symptoms == 'Y' and temperature >= 37:
        clinic_counts[0] += 1 # A 진료소
    elif symptoms == 'N' and temperature >= 37:
        clinic_counts[1] += 1 # B 진료소
    elif symptoms == 'Y' and temperature < 37:
        clinic_counts[2] += 1 # C 진료소
    else:
        clinic_counts[3] += 1 # D 진료소

# 진료소 인원 출력 
print(*(clinic_counts), end="")

# 위급상황 판단 => A로 가는 사람이 2명 이상일 때
if clinic_counts[0] >= 2:
    print(" E")
else:
    print() # 줄바꿈만 수행