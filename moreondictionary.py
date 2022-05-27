#histogram problems
#counting using dictionaries
#problem_ to have alot of words and remembering which word occured most and how many times!!
names=dict()
names['riti']=1
names['shreya']=1
names['sam']=1
names['rud']=1
print(names)
names['sam']=names['sam']+1

for yes in names:
	if yes not in names:
			names[yes]=1
	else:
	    names[yes]=names[yes]+1
print(names)	
#So now we have this dictionary that's kind of growing as time is progressing.
# when we see something new , how to proceed counting

counts=dict()
name=['ram','sam','dam','bam']

 
for ok in name:
	if ok not in counts:
		counts[ok]=1
	else:
	   counts[ok]=counts[ok]+1
print(counts)	    	


