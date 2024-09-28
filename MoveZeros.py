# From a list of numbers move 0 to 
# the end of the list

my_list = [2,0,3,4,0,6,7]

for item in my_list:
    
    if item == 0:
        my_list.remove(0)
        my_list.append(0)
        
print(my_list)        