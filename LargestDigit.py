

def largest_digit(num):
    
    nums = []
    while num > 0:
        rem = num % 10
        nums.append(rem)
        num = num // 10 
        
    maxx = float('-inf')
    
    for n in nums:
        if n > maxx:
            maxx = n 
    
    return maxx        

num = int(input("Enter the number: "))
result = largest_digit(num)

print(result)