
# A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

def check_perfect(num):
    
    sum_of_divisors = 0 
    
    for i in range(1,num):
        if num % i == 0:
            sum_of_divisors += i 
    
    
    return sum_of_divisors == num
    

num = int(input("Enter the number: "))

if check_perfect(num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
    

# 6     ->  1 + 2 + 3 = 6 
# 496   ->  1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496 