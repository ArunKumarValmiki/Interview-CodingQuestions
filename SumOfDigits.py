
def summ_digits(num):
    
    nums = []
    while num > 0:
        rem = num % 10
        nums.append(rem)
        num = num // 10 
        
    summ = 0 
    for num in nums:
        summ += num 
    
    return summ    

num = int(input("Enter the number: "))
result = summ_digits(num)

print(result)