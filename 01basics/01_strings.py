chai="Masala Chai"

slice_chai=chai[0:6]
print(slice_chai)

print(chai[-1]) 
print(chai[-2])
print(chai[-8:-1])

print(chai.lower())
print(chai.upper())

chai2="   lemon chai   "
print(chai2)
print(chai2.strip())
print(chai.replace("Masala","Ginger"))

chai3="Lemon, Masala, Ginger, Mint"
print(chai3.split(", "))

print(chai.find("Chai"))

chai4="Masala Chai Chai Chai Chai"
print(chai4.count("Chai"))

quantity=5
order="I want {} cups of {}".format(quantity, chai)
print(order)

chai_variety=["Masala", "Lemon", "Ginger", "Mint"]
s1=" ".join(chai_variety)
print(s1)

s2="He said, \"I love chai!\""
print(s2)
s3=r"Masala\nChai"
print(s3)

print("Masala" in chai)