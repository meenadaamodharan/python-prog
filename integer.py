import sys
mee,nan=map(int,sys.stdin.readline().split(' '))
l1=list(map(int,input().split()))
var=0
for i in range(nan):
    var=var+l1[i]
print(var)
