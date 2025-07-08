import time

def cache(func):
    cache_dict = {}
    def wrapper(*args):
        if args in cache_dict:
            print("Returning cached result")
            return cache_dict[args]
        else:
            print("Calculating result")
            result = func(*args)
            cache_dict[args] = result
            return result
    
    return wrapper
@cache
def long_running_function(a,b):
    time.sleep(4)
    return a+b

print(long_running_function(2, 3))  # First call, should calculate and cache the result
print(long_running_function(2, 3))  # Second call, should return cached result