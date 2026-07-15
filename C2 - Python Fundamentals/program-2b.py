# ==========================================
# Chapter 2: Literals, Operators & Punctuators (Detailed Book Version)
# File: python-2b.py
# ==========================================

# ==========================================
# 1. NUMERIC LITERALS
# ==========================================
# Concept: Numeric literals refer to numbers used as data. 
# They cannot contain commas. They can have a positive (+) or negative (-) sign.
# In Python, they are mainly of three types: int, float, and complex.

print("--- 1. NUMERIC LITERALS ---")

# A. Integer Literals (int)
# These are whole numbers without any decimal point. 
# In Python 3.x, there is no separate 'long' data type; 'int' handles both small and massive numbers.
# Python allows three types of integers based on their number system:

# i. Decimal Integer (Base 10): Normal numbers (Digits 0-9). Must not start with 0.
dec_int = 1234
# ii. Octal Integer (Base 8): Starts with '0o' or '0O' (zero followed by letter o). Only digits 0-7 allowed.
oct_int = 0o14      # Decimal equivalent is 12 (1x8 + 4)
# iii. Hexadecimal Integer (Base 16): Starts with '0x' or '0X'. Digits 0-9 and letters A-F allowed.
hex_int = 0XC       # Decimal equivalent is 12

print("Integer Types -> Decimal:", dec_int, "| Octal:", oct_int, "| Hexadecimal:", hex_int)


# B. Floating Point Literals (float)
# Also called 'real literals', these are numbers that have a fractional (decimal) part.
# They can be written in TWO forms:

# i. Fractional Form: Contains a decimal point.
frac_1 = 17.5
frac_2 = -0.00625
frac_3 = .3         # Same as 0.3

# ii. Exponent Form: Used for very large or very small numbers.
# It has two parts: Mantissa (before E) and Exponent (after E).
# Rule: Number = Mantissa x 10^Exponent
# Example: 5.8 can be written as 0.58 x 10^1 = 0.58E01
exp_float = 0.58E01  
print("Float Types -> Fractional:", frac_1, "| Exponent:", exp_float)

# 🚨 BOOK WARNING CAUGHT HERE: The Comma Trap!
# If you write a number like 17,250, Python does NOT treat it as a number.
# It treats the comma as a separator and creates a "Tuple" (a sequence of values).
trap_value = 17,250
print("If you use a comma (17,250), it becomes a:", type(trap_value), "Output:", trap_value)


# ==========================================
# 2. BOOLEAN LITERALS
# ==========================================
# Concept: Used to represent truth values. There are ONLY two Boolean values in Python:
# True (Boolean-true) and False (Boolean-false). 
# Note: They are case-sensitive. 'T' and 'F' must be capital.

print("\n--- 2. BOOLEAN LITERALS ---")
is_valid = True
is_empty = False
print("Boolean Values:", is_valid, "and", is_empty)


# ==========================================
# 3. SPECIAL LITERAL (None)
# ==========================================
# Concept: Python has one special literal: None.
# It signifies the 'absence of value'. It means "There is no useful information here".
# It is NOT zero (0 is an integer value). It is NOT an empty string ("").
# Book Fact: If you just type a variable containing None in the interactive shell, 
# Python displays nothing. But if you use print(), it explicitly shows 'None'.

print("\n--- 3. SPECIAL LITERAL None ---")
data_missing = None
print("What does missing data look like?", data_missing)


# ==========================================
# 4. OPERATORS
# ==========================================
# Concept: Operators are tokens that trigger some computation.
# The variables/values they are applied to are called 'operands'.
# Operators are divided into two main categories based on operands:

print("\n--- 4. OPERATORS ---")

# A. UNARY OPERATORS (Require only ONE operand)
# Example: Changing the sign of a single variable.
num = 10
print("Unary Plus (+):", +num)
print("Unary Minus (-):", -num)
# Other unary operators: Bitwise complement (~), Logical negation (not)

# B. BINARY OPERATORS (Require TWO operands)
a = 15
b = 4

# i. Arithmetic Operators
print("Addition (+):", a + b)
print("Remainder/Modulus (%):", a % b)
print("Floor division (//):", a // b)  # Divides and chops off the decimal part

# ii. Relational Operators (Compare values)
# Includes: <, >, <=, >=, == (Equal to), != (Not equal to)
print("Is 15 greater than or equal to 4?", a >= b)

# iii. Logical Operators
# Combine multiple conditions.
# 'and': True if BOTH conditions are True.
# 'or': True if AT LEAST ONE condition is True.
print("Logical AND:", (a > 10 and b < 5))  

# iv. Assignment Operators
# Used to assign values to variables. Include: =, +=, -=, *=, /=, %=, **=, //=
score = 100
score //= 3  # Translates to: score = score // 3 (Assign floor division)
print("After Assignment Operator (score //= 3):", score)

# v. Identity Operators (is, is not)
# Checks if two objects share the SAME memory address.
print("Is 'a' the exact same object as 'b'?", a is b)

# vi. Membership Operators (in, not in)
# Checks if a sequence contains a specific value.
name = "Python"
print("Is 'th' in 'Python'?", 'th' in name)

# vii. Bitwise & Shift Operators
# Bitwise: & (AND), ^ (Exclusive OR / XOR), | (OR)
# Shift: << (Shift Left), >> (Shift Right)


# ==========================================
# 5. PUNCTUATORS
# ==========================================
# Concept: Punctuators are symbols that organize programming-sentence structures.
# Just like English needs commas and full stops to make sense, Python needs punctuators
# to indicate the rhythm, emphasis, and structure of expressions.
# Common punctuators: '  "  #  \  (  )  [  ]  {  }  @  ,  :  .  =

print("\n--- 5. PUNCTUATORS ---")
# Example of Punctuators in action:
info_list = ["Apple", "Banana"]  # Here [ ], "", and , are all punctuators!
print("Punctuators bring structure to the code!")