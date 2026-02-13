N = int(input())
arr = list(map(int, input().split()))
list_arr = [x**2 for x in arr]
print(*list_arr)