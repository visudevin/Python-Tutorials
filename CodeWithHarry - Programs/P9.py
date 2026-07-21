# ==========================================
# Chapter 2: Advanced Print, Line Breaking & Logic
# File: program-2f.py
# ==========================================

print("--- 1. ADVANCED PRINT() FEATURES ---")

# Concept 1: The 'sep' argument
# The print() function automatically converts items to strings before printing.
# It also inserts spaces between items automatically because the default value of the 'sep' argument is a space (' ').
print("My", "name", "is", "Amit.")

# You can change this separator character by specifying the 'sep' argument.
print("My", "name", "is", "Amit.", sep="...")

# Concept 2: The 'end' argument
# The print() statement appends a newline character at the end of the line by default.
# If you explicitly give an 'end' argument, it will print that string at the end instead of going to a new line.
a, b = 20, 30
print("a =", a, end=' ')  # It will leave a space instead of pressing 'Enter'
print("b =", b)


print("\n\n--- 2. BREAKING LONG STATEMENTS ---")

# Concept: In Python, you can break any statement by putting a backslash (\) at the end of the line and pressing Enter.
# This completes the statement in the next line perfectly.
print("Hello Enthusiast,", \
"How do you find Python?")


print("\n--- 3. TRICKY MULTIPLE ASSIGNMENTS ---")

# Concept: Python always evaluates the entire Right-Hand Side (RHS) before assigning values to the Left-Hand Side (LHS).
x, y = 2, 6

# The right-hand side evaluates first: 'y' is 6, and 'x + 2' is 2 + 2 = 4.
# Then it assigns these evaluated values to x and y. So x gets 6 and y gets 4.
x, y = y, x + 2
print("Output of x and y:", x, y)


print("\n--- 4. PRACTICAL: TEMPERATURE CONVERTER ---")

# Program to obtain temperature in Celsius and convert it into Fahrenheit.
# The formula is: C * 9/5 + 32 = F.

# Note: Using hardcoded value for demonstration. In real use, you can use float(input("Enter temp..."))
Cels = 37.5 
Fahr = Cels * 9/5 + 32

print("Temperature in Celsius is :", Cels)
print("Temperature in Fahrenheit is :", Fahr)