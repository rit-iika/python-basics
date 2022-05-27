#Dictionaries at python
#dictionaries are another 2nd kind of data structures.
# its a kind of collection
# collections is python = lists + dictionaries
# LISTS = a linear orderly collection of values that stay in order. we can append at the end. 
# DICTIONARY = is a BAG of values each with its own label. it is messed . they dont always stay in order. BUT THEY ARE SUPER POWERFUL.
# everything inside a dictionary has to have some label and a value . or a KEY and a VALUE.
# dictionaries are pythons most powerful data structures: they allow us to do fast database like operations in python.
#dictionaries have differnt names in diff languages.
#dict are like bages: no order!!!!
#dict contents are mutable:: they can be changed

purse=dict()
purse['money']=13
purse['candy']=5
purse['tissues']=15
print(purse)
print(purse['candy'])
purse['candy']=purse['candy']+2 
print(purse)

#content inside  a dictionary
# dictionary literals use curly braces and then inside are pairs of 'KEY': VALUE
# we can make empty braces by using empty curly braces too

#to check any key is in the dictionary or not ; use IN
#print(names['samuel'])
#traceback error!!
#instead use IN
print('samuel' in names)