def second_minimum():
    
    minn1 = arr[0]
    minn2 = arr[0]
    
    for num in arr:
        if num < minn1:
            minn2 = minn1
            minn1 = num 
        elif num < minn2 and num != minn1:
            minn2 = num
            
    print(minn1)
    print(minn2)
        

arr = [20,10,20,30,55,5,10]
second_minimum()