# Find the remainder of a number without using modulus operator

def find_remainder(num,div):
    
    rem = num - (num // div) * div        # r = a - (a/b) * b
    return rem
    
    
num = int(input("Enter the first number: "))
divisor = int(input("Enter the second number: "))

remainder = find_remainder(num,divisor)

print(f"The remainder is {remainder} when {num} is divided by {divisor}")