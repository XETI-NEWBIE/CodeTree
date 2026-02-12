gender = int(input())
age = int(input())

# man = 0
# woman = 1

if gender == 0 and age>=19:
    print("MAN")
elif gender==1 and age>=19:
    print("WOMAN")
elif gender==0 and age<19:
    print("BOY")
else:
    print("GIRL")