import math

friends = 10

friends = friends + 2
friends += 2

friends = friends -2
friends -= 2

friends = friends * 2
friends *= 2

friends = friends / 2
friends /= 2

friends = friends ** 2
friends **= 2

friends = friends % 2
friends %= 2

x = 625
y = 4
z = 5

result = abs(y)
result = round(x)
result = pow(4, 3)
result = max(x, y, z)
result = min(x, y, z)

print(math.e)
print(math.pi) 
print(math.sqrt(x))
print(math.ceil(9.9))
a = float(input("Enter side A:  "))
b = float(input("Enter side B:  "))
formula = a**2 + b**2  # OR pow(a, 2) + pow(b, 2) 
c = math.sqrt(formula)
print(f"Side C :  {round(c, 3)}")