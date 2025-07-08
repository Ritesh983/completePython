f=open("file1.py")

print(iter(f) is f)  # This will print True, confirming that f is an iterator

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())    #This will raise StopIteration if there are no more lines

# for line in f:
#     print(line,end='')  # end='' to avoid adding extra newlines since lines already contain them

while True:
  line=f.readline()
  if not line:
    break
  print(line,end='')  # end='' to avoid adding extra newlines since lines already contain them