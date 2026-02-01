A,B,C=map(int, input().split())

if (A<B<C) and (C<B<A):
    print(B)
elif (B<A<C) and (C<A<B):
    print(A)
elif (A<C<B) and (B<C<A):
    print(C)
else:
    print(None)