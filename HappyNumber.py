
# A happy number is a number that eventually reaches 1 when it is replaced  by the sum of the sqaures of its digits repeatedly. 


def is_happy(num):
    
    seen_numbers = set()
    
    while num != 1 and num not in seen_numbers:
        seen_numbers.add(num)
        current = num 
        sum_of_sqaures = 0  
        
        while current > 0:
            digit = current % 10 
            sum_of_sqaures += digit ** 2 
            current = current // 10 
        
        num = sum_of_sqaures 
        
    return num == 1     

num = int(input("Enter the number: "))

if is_happy(num):
    print(f"{num} is a happy number")
else:
    print(f"{num} is not a happy number")