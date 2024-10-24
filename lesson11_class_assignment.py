myset = {'apple', 'banana', 'cherry', 'apple', 'orange'}

print("Printing new set: ",myset)

#find union and intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Union is: ",set1 | set2)
print("Intersection is: ", set1 & set2)

newset = set() #Create empty set
newset.update({1,2,3,4}) # Add 1,2, 3, 4 to the set
newset.discard(2) #Remove 2 from the set
print(newset) # Print set

fruits = {'apple', 'banana', 'cherry'} #Given a set

if 'orange' in fruits: #check if 'orange' and 'apple' are in the set.
    print('Orange is in set')
elif 'apple' in fruits:
    print('Apple is in set')

workshop1 = {'John', 'Emma', 'Sophia', 'Mike'} #Hard task - Given two sets of students who attended different workshops:
workshop2 = {'Sophia', 'Mike', 'Olivia', 'Liam'}

#Find the names of students who attended only one of the workshops (not both).
attended_both= workshop1 & workshop2
print("Attended both: ", attended_both)
attended_one=workshop1.symmetric_difference(workshop2)
print("Attended only one: ", attended_one)