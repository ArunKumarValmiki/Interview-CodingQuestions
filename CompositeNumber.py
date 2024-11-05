
# A composite number is a number having factors other than 1 and itself.

def check_composite(num):
    
    if num <= 3:
        return False 
        
    # check divisors from 2 to square root of that number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True              # If any divisor is found, it is a composite, immediately returns True
    
    return False        

num = int(input("Enter the number: "))

if check_composite(num):
    print(f"{num} is a composite number")
else:
    print(f"{num} is not a composite number")