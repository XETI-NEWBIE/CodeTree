a,b,c = input().split()
max_val=0

for i in a,b,c:
    if i>=i[-1]:
        max_val=i
print(max_val)   