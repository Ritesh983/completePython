tea_varities = ["Black", "Green", "Oolong", "White", "Herbal"]

print(tea_varities[0])
print(tea_varities[1:3])


# tea_varities[1:2]="Lemon"
tea_varities[1:2]=["Lemon"]
tea_varities[1:3]=["Green","Masala"]
print(tea_varities)

tea_varities[1:1]=["test", "test"]
print(tea_varities)
tea_varities[1:3]=[]
print(tea_varities)

tea_varities.append("Ginger")
print(tea_varities)
tea_varities.insert(2, "Mint")  
print(tea_varities)
tea_varities.remove("Ginger")     
print(tea_varities)
tea_varities.pop()  
print(tea_varities)
tea_varities.clear()
print(tea_varities)

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

squared_num=[x**2 for x in range(10)]
print(squared_num)
