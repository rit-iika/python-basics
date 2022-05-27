a=[1,4,7,2,9,72]
a.sort()
print (a)

print("using bubble sort \n")
def bubbleSort(arr):
    n=len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[64,34,89,76,101,3]
bubbleSort(arr)

print("sorted array is: ")
for i in range (len(arr)):
    print("%d" %arr[i])
