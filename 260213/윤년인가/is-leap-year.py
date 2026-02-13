
Y = int(input())
# 예외적인 해의 조건 (평년) 을 앞에 먼저 써준다
if Y%400 == 0 :
    print("true")
# 예외적인 해의 조건 (평년) (2) 똑같이 연달아 써주기
elif Y%100 == 0 :
    print("false")
# 그리고 4로 나누어 떨어지는 윤년의 조건식을 작성해준다
elif Y%4 == 0 :
    print("true")
# 위에 전부 해당사항이 아니라면 아니라면 그 해는 평년이다
else:
    print("false")