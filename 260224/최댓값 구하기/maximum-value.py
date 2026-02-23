a,b,c = map(int, input().split())
max_val=a

for i in [a,b,c]:
    if i>=max_val:
        max_val=i
print(max_val)   

# a, b, c = map(int, input().split()) # 정수로 변환
# max_val = a # 일단 첫 번째 숫자가 가장 크다고 가정

# for i in [a, b, c]:
#     if i > max_val: # 현재 들고 있는 최대값보다 i가 더 크면?
#         max_val = i # 최대값을 i로 교체!
        
# print(max_val)