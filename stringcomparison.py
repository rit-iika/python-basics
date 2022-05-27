#stringcomparison
#rule1= uppercase letters are less than lower case ones
#uppercase letters comes before lowercase
#eg: A<a
#eg: Z<z
print("enter any word from letter 'b'")
word='B'
print("you entered: ",word)
if word=='banana':
 print('all right, b')

if word<'b':
 print('your word '+word+', comes before b !')
elif word>'b':
	print('your word '+word+' ,comes after b !')
else:
	print('all right , bananas')
print("exercise done!!")
#here i changed banana-> b
#undo it further
stuff="ritika"
str.capitalize(stuff)
print(stuff)