info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

# Accessing Dictionary items:
# I. Accessing single values:
# Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning keys either in square brackets or by using get method.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('name'))

# II. Accessing multiple values:
# We can print all the values in the dictionary using values() method.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# III. Accessing keys:
# We can print all the keys in the dictionary using keys() method.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# IV. Accessing key-value pairs:
# We can print all the key-value pairs in the dictionary using items() method.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

#Dictionary Methods
# 1.update()
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

# Removing items from dictionary:
# There are a few methods that we can use to remove items from dictionary.

# clear():
# The clear() method removes all the items from the list.
# info = {'name':'Karan', 'age':19, 'eligible':True}
# info.clear()
# print(info)

#pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

# del:
# we can also use the del keyword to remove a dictionary item.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

#If key is not provided, then the del keyword will delete the dictionary entirely.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)