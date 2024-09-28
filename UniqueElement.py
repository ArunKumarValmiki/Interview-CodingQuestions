
def find_unique(arr):
    
    d = {}
    for num in arr:
        if num not in d:
            d[num] = 1 
        else:
            d[num] += 1 
    
    for key,value in d.items():
        if value == 1:
            yield key
            
arr = [3,3,4,2,3,5,6,7,8,9,8,3,4,5,9,6]              # 2,7
results = find_unique(arr)

# print(f"The element appears once is {result}")        # use this statement when return keyword is used.(i.e return key )

for result in results:
    print(result)