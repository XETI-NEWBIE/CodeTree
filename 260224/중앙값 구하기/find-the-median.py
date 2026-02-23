a,b,c = map(int,input().split())

if a>=b:
    if a<=c:
        print(a)
if a<b:
    if a>=c:
        print(a)
if b>=c:
    if b<=a:
        print(b)
if b<c:
    if b>=a:
        print(b)
if c>=a:
    if c<=b:
        print(c)
if c<b:
    if c>=a:
        print(c)