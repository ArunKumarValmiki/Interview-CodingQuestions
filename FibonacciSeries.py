
def fibonacci(n):
    
    fib_series = []
    a, b = 0, 1
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    
    return fib_series    

n = int(input("Enter the number of terms: "))

res = fibonacci(n)

print(f"Fibonacci series upto {n} terms : {res}")