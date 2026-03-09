result=0
sum = 0
cnt=0

while True:
    n=int(input())

    if n<20 or n>=30:
        break

    if 20<=n<30:
       sum += n
       cnt += 1

result = sum / cnt
print(f'{result:.2f}')



