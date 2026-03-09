

while True:
    n = int(input())
    if n==1:
        n='John'
    elif n==2:
        n='Tom'
    elif n==3:
        n='Paul'
    elif n==4:
        n='Sam'
    elif n>=5:
        print('Vacancy')
        break
    print(n)