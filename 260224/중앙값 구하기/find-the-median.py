a,b,c=map(int,input().split())

if (a<=b<=c) or (c<=b<=a):
    print(b)
elif (b<=a<=c) or (c<=a<=b):
    print(a)
else:
    print(c)



# a, b, c = map(int, input().split())

# # a가 중앙값인 경우: b <= a <= c 또는 c <= a <= b
# if (b <= a <= c) or (c <= a <= b):
#     print(a)
# # b가 중앙값인 경우: a <= b <= c 또는 c <= b <= a
# elif (a <= b <= c) or (c <= b <= a):
#     print(b)
# # 위 두 경우가 아니면 당연히 c가 중앙값!
# else:
#     print(c)