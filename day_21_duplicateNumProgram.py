
#I use a set to track seen elements. If an element appears again i mark it as duplicate.

numbers = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,89,9,9]
seen = set()
duplicates = set()
for num in  numbers:
   if num in seen:
      duplicates.add(num)
   else:
      seen.add(num)   
print(duplicates)