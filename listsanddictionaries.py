#lists and dictionaries
# dictionaries are like lists:: they use keys instead of numbers to look up for values.
lst=list() #lists have positions
# we can also delete items from lists
lst.append(10)
lst.append(20)
lst.append(30)
lst.append('meoww')
print(lst)
lst[2]=23
print(lst)

dic=dict()   #dict have labels
dic['money1']=10
dic['money2']=20
dic['money3']=30
print(dic)
dic['-']='meoww'
print(dic)
#The key difference, the significant difference, is that the **key mechanism***,
# and the way we look up an entry inside the collection, is different between them.

list1=[]
list2=[]
num=int(input("no of students: "))
print(num)
for i in range(num):
    name=input("name: ")
    marks=int(input("marks:"))
    list1=[name,marks]
    list2+=[list1]
    print(list2)