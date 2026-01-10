#dictionary
#help(dict)

#access by keys 
#value can change but not keys 
#key should not commmon 
#key ke base rahegi hamari value 
#insertion order follow karti hai

#no index value present 

# d ={10:100,20:200,30:300}
# print(d[30])                     

# d ={10:100,20:200,30:300}
# d.update({30:500})   #or  d[50] = 600  updating
# d[90] = 9000 #creating
# del d[30] #deleting
# print(d)


# d ={10:100,20:200,30:300}
# for i in d:
#     print(d[i]) #for values 
#         # orrrr
# for i in d.values:
#     print(i) #for values 100,200,300



#  d={10:100,20:200,30:300}
# for i in d:
#     print(i)  #for keys 10 20 30

#for sseeing all the items in dic 

# d={10:100,20:200,30:300}
# print(d.items())

#merging both dictionary in one 
# d1={10:100,20:200,30:300}

# d2={50:100,60:200,70:300}

# for i in d2:
#     d1[i] =  d2[i]

# print(d1)    

#sum of both dictionary
# d1={10:100,20:500,30:300}
# sum = 0
# for i in d1 :
#     sum = sum + d1[i]
# print(sum)


#repetation count 
#count freuency of each elements in list that why we take bracket 
# a = [1,1,1,2,2,3,3,3,3,3,4,4,4,5]

# d = {}

# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1
# print(d)        





a = [1,1,1,1,2,2,2,2,2,5,5]

d = {}

for i in a:

    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1
print(d)      
