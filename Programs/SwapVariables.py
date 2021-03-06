
# Traditional way

x = 50
y = 16

temp = x
x = y
y = temp

print(x) # 16
print(y) # 50

-----------------------------------------------------------------------------------------------------

# Python way

x = 50
y = 16

x, y = y, x

print(x) # 16
print(y) # 50

-----------------------------------------------------------------------------------------------------

# Using XOR

x = 50
y = 16

x = x ^ y
y = x ^ y
x = x ^ y

print(x) # 16
print(y) # 50

-----------------------------------------------------------------------------------------------------


# Using Arithatic Operators

x = 50
y = 16

x = x + y
y = x - y
x = x - y

print(x) # 16
print(y) # 50
