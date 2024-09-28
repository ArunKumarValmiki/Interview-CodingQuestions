
def find_second_maximum():
    
    max1 = -float('inf')
    max2 = -float('inf')
    
    for num in arr:
        if num > max1:
            max2 = max1 
            max1 = num 
        elif num > max2 and num != max1:
            max2 = num 
    
    print(max1)
    print(max2)

# arr = [30,10,20,45,88,23]
arr = [2,3,6,6,5]
find_second_maximum()

# print(res)