n=int(input("Enter a number: ") )

if n < 0:
    print("Factorial is not defined for negative numbers.") 
elif n == 0 or n == 1:
    print("Factorial of", n, "is 1.")     
else:
    factorial = 1
    i=1
    while(i <= n):
        factorial *= i
        i += 1
    print("Factorial of", n, "is", factorial)