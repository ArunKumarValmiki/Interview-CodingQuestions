# T.C - O(n)
# S.C - O(1)

def find_min_max(arr):
    
    maxx = float('-inf')
    minn = float('inf')
    
    for num in arr:
        if num > maxx:
            maxx = num 
            
    for num in arr:
        if num < minn:
            minn = num 
            
    return maxx, minn        

arr = [10,5,20,30,25,15]
res, res1 = find_min_max(arr)

print(f"Maximum value : {res}")
print(f"Minimum value : {res1}")