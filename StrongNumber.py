
# A strong number is a number in which the sum of the factorial of each of its digits is equal to the number itself.
# A strong number is also known as factorial number.

def check_strong(num):
    
    if num == 1 or num == 2:
        return True 
        
    original_num = num 
    summ = 0 
    
    while num > 0:
        digit = num % 10 
        fact = 1 
        for i in range(1,digit+1):
            fact = fact * i  
        summ += fact 
        num = num // 10 
    
    if summ == original_num:
        return True 
    return False


num = int(input("Enter the number: "))
print(check_strong(num))


# Upto to 10,00,000
# We have only four strong numbers - 1,2,145,40585