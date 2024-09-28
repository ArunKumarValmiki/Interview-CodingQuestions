# Given two strings s1 and s2 return true if they are anagram

# s1 = 'listen'
# s2 = 'silent'   - true

# s1 = 'rat'
# s2 = 'cat'      - false 


# s1 = 'eleven plus two'
# s2 = 'twelve plus one'



def check_anagram(s1,s2):
    count = 0 
    
    for s in s1:
        if s in s2:
            count += 1 
            
    return count         

    
s1 = input("Enter the string 1: ")
s2 = input("Enter the string 2: ")
count = check_anagram(s1,s2)

n = len(s1)

if n == count:
    print("True")
else:
    print("False")


