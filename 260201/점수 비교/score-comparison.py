a_math, a_english = map(int, input().split())
b_math, b_english = map(int, input().split())

A = a_math, a_english
B = b_math, b_english


if A > B:
    print(1)
else:
    print(0)