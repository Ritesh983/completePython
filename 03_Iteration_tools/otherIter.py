D={'a':1,'b':2,'c':3,'d':4}

I=iter(D)
print(I)
print(next(I))  # This will return the first key in the dictionary
print(next(I))  
print(next(I))  
print(next(I))  
#print(next(I))  # This will raise StopIteration error as there are no more elements in the iterator


R=range(5)
print(R)
I=iter(R)
print(I)
print(next(I))  # This will return the first value in the range
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) 
print(next(I)) # This will raise StopIteration error as there are no more elements in the iterator