
def palindrome(num):
    
    rev = 0
    
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem 
        num = num // 10 
        
    return rev    
    
num = int(input("Enter the number : "))
ans = palindrome(num)

if ans == num:
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")