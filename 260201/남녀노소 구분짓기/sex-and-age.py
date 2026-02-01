gender = int(input())
age = int(input())

man = 0
woman = 1

if gender == man:
    if age>=19:
        print("MAN")
    else:
        print("BOY")
elif gender == woman:
    if age>=19:
        print("WOMAN")
    else:
        print("GIRL")
