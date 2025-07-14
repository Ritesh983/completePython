def chaicoder(num):
  def actual(x):
    return x**num
  return actual
# This function returns another function that raises a number to the power of num

f=chaicoder(2) 
g=chaicoder(3)

print(f)
print(g)

print(f(3))
print(g(3))