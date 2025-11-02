def qms(arr):
    if len(arr)>1:
        
        arr1=[]
        arr2=[]
        arr3=[]
        i=0
        for i in range(len(arr)):
            a=arr[0]
            
            if min(arr)==arr[0]:
                a=arr[1]
            if arr[i]<a:
                arr1.append(arr[i])
            elif arr[i]==a and arr[0]==arr[1]:
                arr3.append(arr[0])
                arr3.append(arr[1])
                break
            else:
                arr2.append(arr[i])
            i=i+1
        qms(arr1)
        qms(arr2)
        
        x=y=z=k=0

        while x<len(arr1):
            arr[k]=arr1[x]
            x=x+1
            k=k+1
        while z<len(arr3):
            arr[k]=arr3[z]
            z=z+1
            k=k+1
        while y<len(arr2):
            arr[k]=arr2[y]
            y=y+1
            k=k+1
        
array=[]
n=int(input("Enter the total no.  of elements:"))
for i in range(0,n):
    m=int(input("Enter the element:"))
    array.append(m)
qms(array)
print("The Sorted Array is ",array)
