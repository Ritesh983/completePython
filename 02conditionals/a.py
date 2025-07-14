age=int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif 13 <= age < 19:
    print("You are a teenager.")  
elif 19 <= age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")