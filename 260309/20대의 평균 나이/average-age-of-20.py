result=0
sum = 0
cnt=0

while True:
    n=int(input())
    sum += n
    cnt +=1

    if n>=30:
        break
    result = sum / cnt  

print(f'{result:.2f}')



