#double splitting
#THE DOUBLE SPLIT PATTERN 
#sometimes we split a line one way and then grab one of pieces of line and split it again
list1='pizza pazta @ macroni cheeseballs chips'
stuff1=list1.split()
print(stuff1)
okay=list1.split('@')
print(okay)
doit=list1.split('@')
print(doit[1])
doit=list1.split()
print(doit[1])