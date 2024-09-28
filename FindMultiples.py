
def find_multiples(num,count):
    multiples = []
    
    for i in range(1,count+1):
        multiples.append(num * i)
    return multiples    


number = int(input("Enter a number to find it's multiples: "))
count = int(input("Enter how many multiples you want to find: "))

multiples = find_multiples(number, count)

print(f"The first {count} multiples of {number} are : {multiples}")