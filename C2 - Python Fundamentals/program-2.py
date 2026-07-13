# ==========================================
# Chapter 2: Python Fundamentals - Practice Code
# ==========================================

# ------------------------------------------
# 1. Variables and Assignments
# ------------------------------------------
print("--- Variables & Assignments ---")

# Multiple Assignments: Assigning values to multiple variables in a single line
a, b, c = 5, 9, 15
print("Multiple Assignment values:", a, b, c)

# Dynamic Typing: A variable's data type can change during execution
dynamic_var = 10
print("Dynamic Type (Int):", dynamic_var)
dynamic_var = "Now I am a string"
print("Dynamic Type (String):", dynamic_var)


# ------------------------------------------
# 2. Simple Input and Output
# ------------------------------------------
print("\n--- Input & Output ---")
# Using print() for output and input() for reading user data
# Note: Uncomment the next two lines to test input functionality in your terminal
# user_age = int(input("Enter your age: ")) 
# print("You are", user_age, "years old.")


# ------------------------------------------
# 3. Literals / Values
# ------------------------------------------
print("\n--- Literals & Values ---")

# String Literals (Single, Double, and Multiline)
single_line = 'Python Tutorials'
multi_line = """This is a multiline string
enclosed within triple double quotes."""
print(single_line)
print(multi_line)

# Numeric Literals (Integer, Float, Complex)
num_dec = 50           # Decimal Integer
num_bin = 0b101010     # Binary Integer
num_oct = 0o320        # Octal Integer
num_hex = 0x12B        # Hexadecimal Integer
float_num = 14.5       # Float
complex_num = 7 + 5j   # Complex (Real + Imaginary)
print("Numeric Literals:", num_dec, num_bin, num_oct, num_hex, float_num, complex_num)

# Boolean Literals (True = 1, False = 0)
bool_calc = True + 3   # 1 + 3 = 4
print("Boolean Arithmetic (True + 3):", bool_calc)

# Special Literal (None)
# None represents the absence of a value (null), not a mathematical zero.
null_value = None
print("Special Literal None:", null_value)


# ------------------------------------------
# 4. Literal Collections
# ------------------------------------------
print("\n--- Literal Collections ---")

# List: Mutable (can be changed), ordered, allows duplicates. Written with []
list_data = ['Python', 'Spidey', 'Anaconda', 2, 5]
print("List:", list_data)

# Tuple: Immutable (cannot be changed), ordered. Written with ()
tuple_data = (2, 4, 6, 8)
print("Tuple:", tuple_data)

# Dictionary: Mutable, stores data in Key:Value pairs. Written with {}
dict_data = {'name': 'Python', 'age': 30, 'type': 'Language'}
print("Dictionary:", dict_data)

# Set: Mutable, unordered, no duplicates. Written with {}
set_data = {'a', 'e', 'i', 'o', 'u'}
print("Set:", set_data)


# ------------------------------------------
# 5. Operators
# ------------------------------------------
print("\n--- Operators ---")

x, y = 10, 3

# Arithmetic Operators
print("Addition:", x + y)
print("Division (Float):", x / y)
print("Floor Division (Int):", x // y)
print("Modulus (Remainder):", x % y)
print("Exponentiation (Power):", x ** y)

# Relational / Comparison Operators (Returns True/False)
print("Is x equal to y?", x == y)
print("Is x greater than y?", x > y)

# Logical Operators (and, or, not)
print("Logical AND:", (x > 5 and y < 5))  # True because both conditions are true
print("Logical OR:", (x > 15 or y < 5))   # True because the second condition is true

# Identity Operators (is, is not)
# Checks if they share the exact same memory location
list1 = [4, 5]
list2 = [4, 5]
print("Are list1 and list2 the same object in memory?", list1 is list2) # False
print("Do list1 and list2 have the same values?", list1 == list2)       # True

# Membership Operators (in, not in)
# Checks if a sequence is present in an object
print("Is 'Spidey' in our list?", 'Spidey' in list_data)

# Bitwise Operators (Compares binary values)
a8 = 0b00000101  # Decimal 5
a9 = 0b00001001  # Decimal 9
print("Bitwise AND (&):", a8 & a9)
print("Bitwise OR (|):", a8 | a9)
print("Left Shift (<<):", a9 << 1)  # Shifts bits left, filling with zero