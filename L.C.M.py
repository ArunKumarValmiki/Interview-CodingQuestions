
def find_lcm(a,b):
    
    greater = max(a,b)
    
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break 
        greater += 1 
        
    return lcm    
    
    
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
lcm = find_lcm(num1,num2)

print(f"L.C.M of {num1} and {num2} is {lcm}")