items=["apple", "banana", "orange", "apple", "mango"]

unique_items= set()

for item in items:
    if item in unique_items:
        print(f"Duplicate item found: {item}")
        break
    else:
        unique_items.add(item)