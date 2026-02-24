a,b=map(int,input().split())
i=a

while i>=a:
    print(i, end=" ")
    if i%2==0:
        i+=3
    elif i%2==1:
        i*=2
    if i>b:
        break
