def find_hcf(x,y):
    
    if x < y:
        smaller = x 
    else:
        smaller = y
    
    for i in range(1,smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i                                 # Break statement not used (since we want largest +ve integer)
            
    return hcf        
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter then second number: "))
res = find_hcf(num1,num2)

print(f"The H.C.F of {num1} and {num2} is {res}")


# easy to understand to implement but not efficient
# T.C = O(min(x,y)) - where x any y are two input numbers
# efficient method - euclidean algorithm