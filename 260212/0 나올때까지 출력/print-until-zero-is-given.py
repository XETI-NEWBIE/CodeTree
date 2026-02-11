

while True:
    try:
        val = int(input())
        if val == 0:
            break
        print(val)
    except EOFError:
        break