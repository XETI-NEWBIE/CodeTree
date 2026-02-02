first, second=map(str, input().split())
# first, second <= 20
if len(first) > len(second):
    print(first, len(first))
elif len(first)  < len(second):
    print(second, len(second))
else:
    print("same")