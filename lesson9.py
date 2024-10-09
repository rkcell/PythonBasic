#INTERNED TUPLE
#
# t1 = ("A", "B")
# t2 = ("A", "B")
#
# print (id(t1))
#
# print (id(t2))



import sys

mylist = [1,2,3,4,5]
mytuple = (1,2,3,4,5)

print("size of tuple", sys.getsizeof(mytuple))
print("size of list", sys.getsizeof(mylist))

mylist.append("ქართული unicode ქართული unicode ქართული unicode ქართული unicode ქართული unicode ქართული unicode ქართული unicode ქართული unicode ქართული unicode")


print("size of list", sys.getsizeof(mylist))


