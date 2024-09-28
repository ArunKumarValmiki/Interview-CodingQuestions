
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                

arr = [30,20,10,45,12,87,65]
bubbleSort(arr)
print("Updated Array: ",arr)

for i,num in enumerate(reversed(arr)):
    if i == 3:
        break 
    print(num)
    