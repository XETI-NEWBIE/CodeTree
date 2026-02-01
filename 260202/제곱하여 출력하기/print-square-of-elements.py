_=input()
N = map(int, input().split())
num=[]
    
for i in N:
    num.append(i**2)

print(*num, end="")