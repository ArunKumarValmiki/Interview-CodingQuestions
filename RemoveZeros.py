
# list1 = [0,0,3,0,5]
# list2 = [1,2,3,0]
list3 = [1,2,3,0,0,0]


for i in range(len(list3)-1,-1,-1):
    if list3[i] != 0:
        break 
    if list3[i] == 0:
        list3.pop()
        
print(list3)        