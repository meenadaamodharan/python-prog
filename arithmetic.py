N,A,D=map(int,input().split())
s=0
for i in range(0,N):
    s=s+A
    A=A+D
print(s)
