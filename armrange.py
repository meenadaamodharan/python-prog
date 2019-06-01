m,n=map(str,input().split())
l=[]
for in range(int(m)+1,int(n)):
    a=0
    x=len(str(i))
    for b in str(i):
        a=a+int(b)**x
    if str(a)==str(i):
        l.append(i)
for b in l:
    print(b,end=" ")
 
   
