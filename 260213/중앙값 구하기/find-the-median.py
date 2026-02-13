A,B,C = map(int, input().split())
# -100<=A,B,C<=100

if (A<B<C) or (C<B<A):
    print(B)
elif (A<C<B) or (B<C<A):
    print(C)
elif (B<A<C) or (C<A<B):
    print(A)