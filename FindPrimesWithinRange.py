import math

lower = int(input("Enter the start range: "))
upper = int(input("Enter the end range: "))

for num in range(lower, upper + 1):
    if num > 1:                # Only check numbers greater than 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break           # If a divisor is found, break out of the loop
        else:
            print(num)          # Executed only if the loop wasn't broken (prime number)
        