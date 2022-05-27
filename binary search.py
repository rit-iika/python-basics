
def search(list,n):
    l=0
    mid=0
    u=len(list)-1

    while l<= u:
        mid= (l+u)//2

        if list[mid]<n:
         l=mid+1

        elif list[mid]>n:
         u=mid-1

        else:
            return mid

    return -1

list=[1,2,3,4,5,6,7,8,9,10,76,87,123,809]
n=87
result = search(list,n)
if result!= -1:
    print("found at ",str(result))
else:
        print("not found")

    