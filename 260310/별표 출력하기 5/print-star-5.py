n=int(input())

# for i in range(n):
#     star = n-i
#     unit = "*" * star + " "
#     print(unit*star)
#     "*"*(n-1)

for i in range(n,0,-1):
    star = "*" * i + " "
    print(star*i)