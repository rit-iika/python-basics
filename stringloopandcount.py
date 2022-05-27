#strings looping and counting
word='banana'
print(word)
count=0
count2=0
for letter in word:
	if letter=='a' :
	  count=count+1
print('number of a: ',count)
for letter in word:
    if letter=='n' :
      count2=count2+1
print('number of n: ',count2)	
 
for letter in word:
	print(letter)