s=input()
n=[]
for char in s:
	if char not in n:
		n.append(char)
print(len(n))
