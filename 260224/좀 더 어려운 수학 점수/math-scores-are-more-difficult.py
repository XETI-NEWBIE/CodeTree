a_math, a_eng = map(int,input().split())
b_math, b_eng = map(int, input().split())

if a_math==b_math:
    if a_eng>b_eng:
        print("A")
    elif b_eng>a_eng:
        print("B")
elif a_math>b_math:
    print("A")
elif a_math<b_math:
    print("B")