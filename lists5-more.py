#list
#searching inside a list
#python provied two operators to check if an item is in list or not- IN and NOT IN
#these are logical operators that return true/false
#they do not modify the list
num=[1,2,3,4,5]
9 in num
#>>false
5 in num
#>>true
20 not in num
#>>true
## calculations in lists
nums=[1,2,3,4,5,6,7,8,9,999]
print(nums)
print("length is :",len(nums))
print("max is :",max(nums))
print("min is :",min(nums))
print("sum is :",sum(nums))
print("sum/len :",sum(nums)/len(nums))
#we can do calculations easily if the list is numeric. even better than we did using loops!!