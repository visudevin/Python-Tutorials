# ==========================================
# CodeWithHarry - Program 6 (Dictionaries & Methods)
# File: p6.py
# ==========================================

# ------------------------------------------
# 1. Basics of Dictionaries, Tuples, and Lists
# ------------------------------------------
d = {} # Empty Dictionary
t = () # Empty Tuple
l = [] # Empty List

print("Type of d:", type(d))
print("Type of t:", type(t))
print("Type of l:", type(l))

# Dictionaries are Key-Value pairs
dz = {"harry": "pytho"}
print("\nValue of key 'harry' in dz:", dz["harry"])

d2 = {'harry': 'python'}
print("Value of key 'harry' in d2:", d2['harry'])

# Adding a new key-value pair to a dictionary
d2['abs'] = 'abesit'
print("d2 after adding new item:", d2)

# ------------------------------------------
# 2. Nested Dictionaries & Modification
# ------------------------------------------
# Dictionary ke andar ek aur dictionary!
d1 = {
    "harry": "python", 
    "visu": {
        "me": "eggs", 
        "visu": "maggie", 
        "her": "velvet cake"
    }
}

# Adding new elements to d1
d1['Ana De Armas'] = 'junk food'
d1[430] = 'kahdoos'

print("\nAccessing nested dictionary (visu -> me):", d1['visu']['me'])
print("d1 after additions:", d1)

# Deleting an element using the 'del' keyword
del d1[430]
print("d1 after deleting key 430:", d1)

# ------------------------------------------
# 3. Dictionary Functions & References
# ------------------------------------------
print("\n--- Dictionary Functions ---")

# The Assignment Trap (Reference)
# d3 = d1 means d3 and d1 point to the EXACT SAME memory location.
# If you delete from d3, it deletes from d1 too!
# d3 = d1 
# del d3['harry'] # Doing this would affect d1 as well.

# The Right Way: copy()
# d3 = d1.copy() creates a fresh, separate copy of the dictionary.
d3 = d1.copy()
del d3["harry"]
print("d3 (Fresh Copy with 'harry' deleted):", d3) #d3 se harry gayab hoga bcz copy fun ne d1 ki copy banakar d3 me dala so, d3 me edit karne par only d3 me changes aayega naki d1
print("d1 (Original remains completely intact):", d1)

#but ha agar d3 = d1 hai lets suppose, so jab d3 me kuchh change hota hai to wo actual me d1 me bhi change aayega. bcz d1 ki copy nahi bani so d3 me change karna matlab d1 me change karna.

# get() method returns the value for a key without throwing an error if the key doesn't exist
print("\nUsing get() for 'harry':", d1.get('harry'))

# update() appends a new dictionary's key-value pairs to the existing one
d1.update({'leena': 'Cake'})
print("d1 after update():", d1)

# keys() returns a list of all the keys in the dictionary
print("\nKeys in d1:", d1.keys())

# items() returns a list of all key-value pairs (as tuples)
print("Items in d1:", d1.items())