
# #self notes for list methods (functions) practice 


 

# l = [-54,54,21,-56,-54,+65,2]  # use[] for the list 
# l.append(9)  # adds the new value at the end 
# l.insert(1,99) # inserting  the value at given index 
# l.extend([20]) #value added at the last 
# l.insert(0,20) #insert the new value by giving new value with index and value
# l.pop(1)  #removes the element by givind index
# l.remove(2) #vremoves the number from the list 
# l.index(21)#gives the index value of that number 
# l.reverse()#reverse the value
# l.sort()
# print(f"{l.index}")
# print (l)






# # question 
# #positive and negative number

# # for i in l:
# #     if i >= 0:  #for positive and negative number 
# #         print(i)





# #extend()
# l1 = [11,12,25,24,]
# l2 = [12,45,45]
# l1.extend(l2)
# print(f" new list is = {l1}")





# #copy()

# l1 = [11,12,25,24]

# l2 = l1.copy()
# print(l2)
#average of list 
# l = [22,12,4,2,1,3]
# sum = 0
# for i in l:
#     sum = sum + i 
# print(f"the sum of all list nnumber is {sum}")
# print(f"the average of the list is = {sum//len(l)}")




# largest number 
# l = [22,12,4,2,99,1,3]
# largest = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > largest :
#         largest = l[i]
#         index = i
# print (f"your largest number is {largest} at index {index}")



# largest number 
# l = [22,11,1515,1545,1548,995,955296,9532]
# highest =l[0]
# index = 0
# for i in range (len(l)):
#     if l[i] >  highest:
#        highest = l[i]
#        index = i
# print(f"{highest} and {index}")



#example for practice 
# l = [115451,121,151512,412,5841,8451,48541,84512154]

# less = l[0]
# index = 0

# for i in range (len(l)):
#     if l[i] < less:
#        less = l[i]
#        index = i
# print(less,index)    



#without index we also fing largest and shortest number 

# l  = [232,1215,1215,12,1521,12]
# less = l[0]
# for i in l:
#     if i < less:
#         less = i
#print(less)



#second largeest number 

# l = [12,23,56,48,96,98,788,985,984]
# largest = l[0]
# sec_largest = l[0]

# for i in l:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest:
#         sec_largest = i

# print(f"largest number is {largest} and\nsecond largest number is {sec_largest}")



#sorted()  sorting means number are  low to high 

# l = [12,25,45,55,85,4,52,6315,1]

# sorted = l.sort()
# print(l)


# #or by using sorted()
# l = [12,25,45,55,85,4,52,6315,1]
# sortedList = sorted(l)
# print(sortedList)


