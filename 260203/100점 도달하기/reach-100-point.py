scores = list(map(int, input().split()))

for num in scores:
    if num >= 90:
        print("A")
    elif num >= 80:
        print("B")
    elif num >= 70:
        print("C")
    elif num >= 60:
        print("D")
    else:
        print("F")
        
# 마지막에 숫자를 찍고 싶다면 for문 밖에서 num 출력
print(num, end=" ")