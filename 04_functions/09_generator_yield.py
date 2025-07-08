def even_generator(n):
    for i in range(2, n + 1, 2):
        yield i
# yield is a keyword that allows the function to return a generator object
# A generator is a special type of iterator that generates values on the fly and can be iterated over without storing all values in memory at once.
for num in even_generator(10):
    print(num)