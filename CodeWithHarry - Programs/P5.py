# ==========================================
# CodeWithHarry - Program 5 (Tuples & Variable Swapping)
# File: p5.py
# ==========================================

# ------------------------------------------
# 1. Mutable vs Immutable Concepts
# ------------------------------------------
# Mutable: Data that can be changed (e.g., Lists).
# Immutable: Data that cannot be changed once created (e.g., Tuples).

tp = (1, 2, 3)
print("Original Tuple:", tp)

# Tuples are immutable, so trying to reassign a value will throw a TypeError.
# tp[1] = 8  # Uncommenting this line will crash the program.
print("Tuple after attempted change:", tp)

# ------------------------------------------
# 2. Single Element Tuple
# ------------------------------------------
# To create a tuple with a single element, you MUST add a comma after the value.
# Without the comma, Python treats (1) just as an integer.
cd = (1,)
print("Single element tuple:", cd)
print("Type of cd:", type(cd))

# ------------------------------------------
# 3. Variable Swapping
# ------------------------------------------
a = 1
b = 2
print("\nBefore swapping: a =", a, ", b =", b)

# Traditional method using a temporary variable (Common in C/C++/Java):
# temp = a
# a = b
# b = temp
# print("After traditional swap: a =", a, ", b =", b)

# The Pythonic Way: Swapping values in a single line without a temp variable!
a, b = b, a
print("After Pythonic swap: a =", a, ", b =", b)