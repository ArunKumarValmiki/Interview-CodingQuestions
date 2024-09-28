
def find_fact(num):
    
    if num == 0 or num == 1:                   # Base case
        return 1 
    else:
        return num * find_fact(num-1)

num = int(input("Enter the number: "))
res = find_fact(num)

print(f"The factorial of {num} is {res}")

# T.C = O(2^n)
# S.C = O(n)