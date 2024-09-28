def findLargest(n):
    
    large = -float('inf')
    
    while n > 0:
        rem = n % 10 
        
        if rem > large:
            large = rem 
            
        n = n // 10  
        
    return large
    
n = int(input("Enter the number: "))   

largest = findLargest(n)  
print(f"The largest digit is {largest}")