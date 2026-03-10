n=int(input())

n = int(input())

for i in range(n):
    # 1. 줄마다 찍힐 별의 개수 (4, 3, 2, 1 순서)
    star_count = n - i
    
    # 2. '별 뭉텅이 + 공백'을 한 단위로 만들기
    # 예: star_count가 4라면 "**** " 가 됨
    unit = "*" * star_count + " "
    
    # 3. 이 단위를 star_count만큼 반복해서 출력
    print(unit * star_count)