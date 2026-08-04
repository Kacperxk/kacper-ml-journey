# Exercise 1.1


# Block A
a = [1, 2, 3]
b = a
b.append(4)
print(a) # [1, 2, 3, 4] - list is mutable
print(b) # [1, 2, 3, 4]
print(a is b) # True - it's the same object
#Due to list mutabilty, assigning it to a new value creates just new name for it

# Block B
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a) # [1, 2, 3]
print(b) # [1, 2, 3, 4] - by using copy() new object was created
print(a is b) # False - different object

# Block C
x = 5
y = x
y += 1
print(x) # 5
print(y) # 6
print(x is y) # False - adding 1 to y rebinds it to new int

# Block D
s1 = "Hello"
s2 = s1
s2 = s2 + " world"
print(s1) # Hello
print(s2) # Hello world - string is also immutable

# Mutation doesn't change memory identity (A/B), while rebinding creates new object (C/D)


# Exercise 1.2


# Version 1 - buggy
def append_to(element, to=[]):
    to.append(element)
    return to

print(append_to(1)) # [1]
print(append_to(2)) # [1, 2]
print(append_to(3)) # [1, 2, 3]
# to=[] is created only once

# Version 2 - correct
def append_to_fixed(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to

print(append_to_fixed(1)) # [1]
print(append_to_fixed(2)) # [2]
# Version 2 creates fresh list inside the call

def make_config(lr=0, epochs=0, hidden_sizes=None):
    if hidden_sizes is None:
        hidden_sizes = [128, 64]
    return hidden_sizes

c1 = make_config()
c2 = make_config()
c1.append(999)
assert c2 == [128, 64]


# Exercise 1.3


import copy
original = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# Shallow copy
shallow = original.copy()
shallow[0][0] = 99
print(original[0][0]) # 99 - changed
# copy() just copied references to the current list

# Deep copy
original2 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
deep = copy.deepcopy(original2)
deep[0][0] = 999
print(original2[0][0]) # 1 - didn't change
# deepcopy creates whole new object at every level of nesting
# Shallow copy create a new container but keeps old references. Deep copy creates new objects

def safe_clone(data: list) -> list:
    return copy.deepcopy(data)

nested = [[[1,2],[3,4]],[[5,6],[7,8]]]
cloned = safe_clone(nested)
cloned[0][0][0] = 999

assert nested[0][0][0] == 1, "deep clone not working"


# Exercise 1.4


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b) # True - objects have identical content
print(a is b) # False - objects share different memory
print(a is c) # True - c is new name for a. Same memory

# Small integer caching - Python caches small ints
x = 256
y = 256
print(x is y) # True - numbers to 256 are already cached and are referring to already created object

x = 257
y = 257
print(x is y) # True in this case

# String interning
s1 = "hello"
s2 = "hello"
print(s1 is s2) # True

s3 = "hello world"
s4 = "hello world"
print(s3 is s4) # Might be False - it's True

# x is y and s3 is s4 prints True in this case, but not because
# of real caching, but because both literals live in the same compiled file