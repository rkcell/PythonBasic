# Task 1: Find the Maximum in a List
# Write a function that takes a list of numbers and returns the largest number in the list.

input_list=[1,2,4,6,8,9,34,5,3,2]

def max_list(mylist):
    x = 0
    for i in mylist:
        if x < i:
            x=i
    return x

print(max_list(input_list))


# Task 2: Remove Duplicates from a List
# Create a function that takes a list of items and returns a new list with all duplicates removed.

dub_list=[2,3,5,7,3,1,6,7,0,5,5]

def remove_duplicate(mylist):

    #return list(set(mylist))
    new_list=[]

    for i in mylist:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicate(dub_list))

# Task 3: Concatenate Two Tuples
# Write a function that accepts two tuples and returns a new tuple that is the result of concatenating
# them.

x1= (1,2,5,7,9)
x2=(2,45,6,7)

def concat_tuples(t1, t2):
    #return t1 + t2
    new_list=[]
    for i in t1:
        new_list.append(i)
    for j in t2:
        new_list.append(j)
    return tuple(new_list)

print(concat_tuples(x1,x2))

# Task 4: Reverse a List
# Write a function that takes a list and returns a new list with the elements in reverse order.

def reverse_list (lst):
    return lst[::-1]

print(reverse_list([1,2,3,4,5]))

# Task 5: Access Tuple Elements by Index
# Create a function that accepts a tuple and prints each element of the tuple along with its index.

def tup_elements(tupl):
    for i in range(len(tupl)):
        print(f"Element at index {i} is {tupl[i]}")

tup_elements((5,4,3,2,1))