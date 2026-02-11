arr = [list(map(int, input().split())) for _ in range(4)]
row = 4
cols=4

count=0

for row in arr:
    for cols in row:
        if cols%5==0:
            count+=1
print(count)