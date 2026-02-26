n=int(input())
cnt_toilet=0
cnt_bokdo=0
cnt_room=0

for i in range(1,n+1):
    if i%12==0:
        cnt_toilet+=1
    elif i%3==0:
        cnt_bokdo+=1
    elif i%2==0:
        cnt_room+=1
print(cnt_room, cnt_bokdo, cnt_toilet, end=" ")
