#Text type: str
# numeric Types: int, float, complex
# sequence types: list, tuple, range
# mapping type: dict
# set types: set, frozenset
# boolean type: bool
# binary types: bytes, bytearray, memoryview

#getting the data type
x = 5
print(type(x))

y = "john"
print (type(y))

z = ["apple", "banana", "cherry"]
print (type(z))

x1 = {"name": "john", "age": 36}
print (type(x1))

x2 = frozenset ({"apple", "banana", "name", "age"})
print (type(x2))

x3 = True
print (type(x3))

x = list(("apple", "banana", "cherry"))
