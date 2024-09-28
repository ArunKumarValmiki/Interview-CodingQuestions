
def sumFisrtLast(n):

    my_list = []
    
    while n > 0:
        rem = n % 10
        my_list.append(rem)
        n = n // 10 
    
    first_digit = my_list[0]
    last_digit = my_list[len(my_list)-1]
    
    return first_digit + last_digit

n = int(input("Enter the number: "))
res = sumFisrtLast(n)

print(f"The sum of first and last digit of {n} is {res}")