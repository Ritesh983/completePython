def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_kwargs(name="Alice", age=30, city="New York")
print_kwargs(name="Bob", age=25, country="USA", hobby="Reading")
print_kwargs()  
print_kwargs(key1="value1", key2="value2", key3="value3")
print_kwargs(a=1, b=2, c=3, d=4, e=5)  
print_kwargs(x="Hello", y="World")  