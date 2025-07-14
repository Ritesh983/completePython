def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # Output: 15
print(sum_all(10, 20, 30))      # Output: 60  
print(sum_all(5))                # Output: 5
print(sum_all())                