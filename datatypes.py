# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x=7
print(x)
y=3+8j
print(y)
z=9.23
print(z)

print(type(z), type(x), type(y))

x=12
print(id(x))
x=15
print(id(x))
# address of same named variables are not same, they are stored in diff places
a=12
print(id(a))
b=12
print(id(b))
# same value variables are stored in same vars