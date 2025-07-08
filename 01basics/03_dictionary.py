chai_types={"Masala": "Spicy","Ginger":"Zesty","Green":"Mild"}
print(chai_types["Masala"])

chai_types.get("Ginger", "Not Found") 

chai_types["Green"]="Fresh"
print(chai_types)

for chai in chai_types:
     print(chai)

for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

chai_types["Mint"]="Refreshing"
print(chai_types)

chai_types.pop("Masala")
print(chai_types) 
chai_types.popitem()
print(chai_types)
del chai_types["Ginger"]
print(chai_types)

#dictionary of dictionaries
chai_varieties = {
    "Masala": {"type": "Spicy", "caffeine": True},
    "Ginger": {"type": "Zesty", "caffeine": True},
    "Green": {"type": "Mild", "caffeine": False}
}
print(chai_varieties["Masala"])
print(chai_varieties["Ginger"]["type"])

square_numbers = {x: x**2 for x in range(5)}
print(square_numbers)
square_numbers.clear()
print(square_numbers)

keys=["Masala", "Ginger", "Green"]
default_values="Spicy"
new_dict=dict.fromkeys(keys, default_values)
print(new_dict)
new_dict2=dict.fromkeys(keys,keys)
print(new_dict2)