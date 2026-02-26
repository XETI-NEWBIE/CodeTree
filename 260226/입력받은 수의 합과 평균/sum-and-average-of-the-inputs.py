n=int(input())
sum=0
average=0

for _ in range(n):
    num=int(input())
    sum+=num

average = sum/n

print(f'{sum} {average:.1f}')
