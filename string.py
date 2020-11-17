x = "Hello. Worlds"
print(x[1])
print(x[0])

# slicing
b = "hello, worlds"
print(b[2:5])
print(b[2:10])
print(b[-6: -4])
print(len(b))

x1 = "hello, worlds, guys  "
print(x1.strip())

a = "hello, worlds, GUY"
print(a.lower())
print(a.upper())

# replace
a = "hello, worlds"
print(a.replace("h", "j"))
print(a.split())

txt = "the rain in spain stays mainly in the plain"
x = "ain" in txt
print(x)
y = 'ain' not in txt
print(y)

# merge variables
a = "hello"
b = "worlds"
c = a + " " + b
print(c)

# use the format() method to insert numbers into strings:
age = 35
txt = "my name is john, and I'm {}"
print(txt.format(age))

# complex format()
quantity = 3
itemno = 35
price = 34.224
myorder = "I want to {0} prices of item {2} for {1} orders and dollars"
print(myorder.format(quantity, itemno, price))

