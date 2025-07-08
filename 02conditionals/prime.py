num=int(input("Enter a number: "))
if num < 0:
    print("Negative number")  
flag=True
for j in range(2,num):
        if num % j == 0:
            flag=False
            break

if flag:
    print(num, "is a prime number")
else:
      print(num, "is not a prime number")