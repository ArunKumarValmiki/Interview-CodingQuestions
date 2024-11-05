
# An armstrong number is a number in which the sum of its digits, each raised to the power of number of digits, is equal to the number itself.
# An armstrong number is also known as the narcissistic number.


def check_armstrong(num):
    
    for i in range(1,10):
        if num == i:
            return True 
            
    num_digits = len(str(num))
    original_num = num 
    summ = 0 
    
    while num > 0:
        rem = num % 10 
        summ += rem ** num_digits 
        num = num // 10 
    
    if summ == original_num:
        return True 
    return False    

num = int(input("Enter the number: "))
print(check_armstrong(num))


# 153(number of digits = 3) ->   1^3 + 5^3 + 3^3 = 153 
# 9474(n = 4)               ->   9^4 + 4^4 + 7^4 + 4^4 = 9474  


