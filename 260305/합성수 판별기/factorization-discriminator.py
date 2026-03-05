# arr = input().split()
# a, b = int(arr[0]), int(arr[1])

# satisfied = False
# for i in range(a, b + 1):
#     if i % 2 == 0:
#         satisfied = True

# if satisfied == True:
#     print("Exists")
# else:
#     print("Not exists")

n = int(input())
# a = n
# # a = (2<=a<=n-1)

# if a>=2 and a<=n-1:
#     if n%a ==0:
#         print('C')
#     else:
#         print('N')

satisfied = False

for i in range(2,n):
    if n%i=0:
        satisfied = True
    
if satisfied == True:
    print('C')    
else:
    print('N')