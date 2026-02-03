
N = int(input())

for num in range(N, 1010):
  	if num >= 90:
       print("A", end=" ")
    elif num >= 80:
       print("B", end=" ")
    elif num >= 70:
        print("C", end=" ")
    elif num >= 60:
       print("D", end=" ")
    else:
		print("F", end=" ")
  
print(num, end=" ")
