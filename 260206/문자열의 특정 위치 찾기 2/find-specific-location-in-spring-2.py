answer = input()
fruits = ["apple","banana","grape", "blueberry", "orange"]
count = 0

for pick in fruits:
    if answer == pick[2] or answer == pick[3]:
        print(pick)
        count+=1

print(count)
    