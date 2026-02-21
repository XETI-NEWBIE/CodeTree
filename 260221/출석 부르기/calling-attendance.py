# 1. 출석부 데이터를 딕셔너리로 만듭니다. (번호: 이름)
attendance_book = {
    1: "John",
    2: "Tom",
    3: "Paul"
}

# 2. 확인하고 싶은 출석번호를 입력받습니다.
# 입력 예제 1번처럼 숫자만 들어오므로 int로 형변환 해줍니다.
try:
    student_num = int(input())

    # 3. 딕셔너리에 해당 번호(key)가 있는지 확인합니다.
    if student_num in attendance_book:
        # 번호가 있으면 해당 이름을 출력
        print(attendance_book[student_num])
    else:
        # 번호가 없으면 Vacancy 출력
        print("Vacancy")
        
except ValueError:
    # 혹시라도 숫자가 아닌 값이 들어올 경우를 대비한 예외 처리
    print("Vacancy")