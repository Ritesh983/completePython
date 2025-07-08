tea_types=("Masala", "Ginger", "Green", "Mint")
print(tea_types[0])
print(tea_types[1:3])
print(tea_types[-1])
print(len(tea_types))

more_tea=("Lemon", "Herbal")
all_tea=tea_types + more_tea
print(all_tea)

t2=("lemon","lemon","lemon","herbal")
print(t2.count("lemon"))
print(t2.index("herbal"))

(black, green, oolong, white) = tea_types
print(black)
print(type(tea_types))

t3=("Lemon",(1,2,3),"Mint")
print(t3)