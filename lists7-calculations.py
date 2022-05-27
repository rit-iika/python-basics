#list calculations
nums=list()
while True:
	inp=input("enter a number: ")
	if inp =='done' : break
	value=float(inp)	
	nums.append(value)
avg	=sum(nums)/len(nums)
print("average : ",avg)