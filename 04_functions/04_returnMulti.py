import math
def cir_stats(radius):
    
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circumference, area

c,a= cir_stats(5)
print(f"Circumference: {c:.2f}, Area: {a:.2f}")