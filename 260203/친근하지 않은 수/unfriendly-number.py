
N = int(input())
count=0

for num in range(1, N+1):
    if num%2==0:
        continue
    elif num%3==0:
        continue
    elif num%5==0:
        continue
    count+=1
print(count)