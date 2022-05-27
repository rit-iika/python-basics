#lists spliting
#split breaks a string into parts and produces a list of strings
#string() function takes up a string and give us back a list
#string()= string->list
# we can access a particular word of string using split()
list='my name is khan'
print("the normal string is:", list)
okay=list.split()
#print("here is the split version:",okay)
#print(okay[0])
#print(okay[1])
#print(okay[2])
#print(okay[3])
print(okay)
for h in okay: #here h is the iteration variable
  #print(okay)
  print(h)
#more on splits
#split counts more whitespaces as just a single one
name='la la          land la '
let=name.split()
print(let)
# we can tell split to split on basis of white char, comma, colon etc etc
#we can tell what delimiter char to use in splittingh
#when we dont specify a delimiter, multiple spaces are treated like one delimiter.
list1='pizza pazta macroni cheeseballs chips'
stuff1=list1.split()
print(stuff1)
stuff1=list1.split(' ')
print(stuff1)
stuff1=list1.split(';')
print(stuff1)
stuff1=list1.split('&')
print(stuff1)
list2='chhole;bhature;pav;bhaji'
stuff2=list2.split()
print(stuff2)
stuff2=list2.split(':')
print(stuff2)
stuff2=list2.split('-')
print(stuff2)