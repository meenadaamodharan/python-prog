ly=int(input())
if ly%4==0 or ly%100==0 and ly%400!=0:
	print("Leap year")
else:
	print("Not a leap year")
