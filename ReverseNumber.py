def reverseNumber(num):
    
    rev = 0
    
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10 
        
    return rev    
    
num = int(input("Enter the number: "))
ans = reverseNumber(num)

print(f"The reverse of a given number is {ans}")
    