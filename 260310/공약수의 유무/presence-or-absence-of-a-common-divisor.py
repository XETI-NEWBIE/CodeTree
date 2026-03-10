a, b = map(int, input().split())

# 1. 일단 공약수를 찾았는지 저장할 변수 (처음엔 없으니까 0)
exists = 0

# 2. A부터 B까지 하나씩 확인해보기
for i in range(a, b + 1):
    # 3. i가 1920의 약수이면서 동시에 2880의 약수인지 확인
    if 1920 % i == 0 and 2880 % i == 0:
        exists = 1
        break  # 하나라도 찾았으면 더 볼 필요 없으니 탈출!

# 4. 최종 결과 출력
print(exists)