#lists2
#RANGE
#RANGE function is special kind of function that we use mostly when we are dealing with loops, but here range() returns a list.
#it returns a list 0 upto not including the number
print(range(2)) #reason -> indecis begin with zeroes
print(range(8))

fruits=['chickkoo','berries','oranges']
print(len(fruits))
print(range(len(fruits)))
#
#
food=['pasta','maggi','bhature']
for eat in food:
	print("i would have one: ",eat)

for i in range(len(food)):
	eats=food[i]
	print("i want some: ",eats)