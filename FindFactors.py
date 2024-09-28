def find_factors(num):
    
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors        



number = int(input("Enter the number: "))

factors = find_factors(number)

for factor in factors:
    print(factor)



