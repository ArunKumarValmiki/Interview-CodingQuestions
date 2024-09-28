
def find_leap(y):
    
    if y % 4 == 0 and y % 100 !=0:
        print(f"{y} is a leap year")
    elif y % 400 == 0:
        print(f"{y} is a leap year")
    else:
        print(f"{y} is not a leap year")

y = int(input("Enter the year: "))
find_leap(y)
