a,b = map(int,input().split())

def uclid(c,d):
        while d:
                c, d = d, c % d
        return c

c = uclid(a,b)


for i in range(a,b+1):
    if i==c:
        print(1)
    else:
        print(0)
            

#