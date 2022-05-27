#lists
#upto now we have been using normal variables, data structures are structured variables. ALGORITHM (is a set of rules we use to solve a problem)
#DATA STRUCTURE is a particular way of organizing data in a computer
#DATA STRUCTURES include lists, tuples and dictionaries.
x=4
x=2
print(x)
# like the variables we declare have just one value in it. if i add another value, older one gets replaced.
#while in a list , a list is a collection, this means that in a single variable we can have more than one value.
#A LIST IS A KIND OF COLLECTION.
x=8 # is a variable
x=[8] # is a list 
#COLLECTIONS ENABLE US TO PUT MANY VALUES IN ONE SINGLE VARIABLE.
friends=['sara','lily','robert']
print(friends)


classi=[["chetan",89],["nayan",87],["shruti",90]]
print(classi)
#square bracket is a list constant
  

#ABOUT LISTS
#list constant are sorrounded by square brackets and elements are separated by comma
#it can be collection of any kind of data, evem a list can be a collection of another list
#a list can be empty
#
print([1,2,6])
print(['seju', 64 ,'rud'])
print([1,2,3,[5,6,7],8])
print([ ])
#we have already used lists in loops.
#lists and definite loops are best friends, they go hand in hand
#lists is a collection in which we can store things anddd also we can extract from them
# INDEX OPERATOR the same operator we used to look inside strings , is used here to look inside lists.
#just like strings, we can get single element of list using an index specified in square brackets.
food=['maggi','pasta','pizza','rolls']
print(food[1])
print(food[2])
#lists are mutable
#strings are immutable ; we cannot change the content of strings. to replace, we have to make a new string
#LISTS are mutable.we can change an elemnt of string, using INDEX OPERATOR
fruit='Banana' #coz this is a string
#fruit[0]='b'
#traceback error !!!!
x=fruit.lower()
print(x)
#thus such operations like lower etc,copies the string and then create a new one. it does not changes into the original string.
#thisnis why we say, that strings are mutable
numbers=[1,2,3,3,5,6,7]
print([numbers])
numbers[3]=4
print([numbers])
#LISTS HAVE LENGTH
#we use same LEN() function to find how lonmg a list is
#len() function uses list as parameter and returns number of elements.
list=['sara', 9.088, 102,'box']
print(len(list))

y=int(len(list))+5
print(y)
