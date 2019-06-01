x=input()
l=len(x)
a=0
for i in x:
    a=a+int(i)**l
if str(a)==str(x):
    print("yes")
else:
    print("no")
