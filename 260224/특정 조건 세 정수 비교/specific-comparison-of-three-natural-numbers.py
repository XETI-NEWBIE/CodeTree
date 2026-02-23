a,b,c=list(map(int,input().split()))
num_list=a,b,c
min_idx=[0]

if a<=b and a<=c:
    min_idx=a
elif b<=a and b<=c:
    min_idx=b
elif c<=a and c<=b:
    min_idx=c

if num_list[0]==min_idx:
    print(1, end=" ")
else:
    print(0, end=" ")

if num_list[0] == num_list[1] == num_list[2]:
    print(1, end=" ")
else:
    print(0, end=" ") 