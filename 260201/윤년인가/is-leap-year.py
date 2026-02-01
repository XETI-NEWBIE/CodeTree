
Y=int(input())

Leap = "true"
Common = "false"

if Y%4==0:
    print(Leap)
    if Y%100==0 and Y%400!=0:
        print(Common)
else:
    print(Common)