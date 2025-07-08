import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate elapsed time
        print(f"Function '{func.__name__}' took {elapsed_time} seconds to execute.")
        return result  # Return the result of the original function
    return wrapper 

@timer
def example_function(n):
    time.sleep(n)  # Simulate a delay

example_function(2)