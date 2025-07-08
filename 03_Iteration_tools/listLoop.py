myList=[1,2,3,4]
I=iter(myList)
print(I)

print(iter(myList) is myList)  # This will return False because iter(myList) creates a new iterator object

print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())
print(I.__next__())  # This will raise StopIteration error as there are no more elements in the iterator
