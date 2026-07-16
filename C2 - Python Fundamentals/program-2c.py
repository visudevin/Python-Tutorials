# ==========================================
# Chapter 2: Barebones of a Python Program
# File: program-2c.py
# ==========================================

print("--- 1. EXPRESSIONS VS STATEMENTS ---")

# 1. EXPRESSIONS
# Concept: An expression is any legal combination of symbols that represents a value.
# Think of it like a math question that gives you an answer (evaluates to a value).
# Examples of expressions: 15, 2.9, a - 5, (3 + 5) / 4.
expression_result = (3 + 5) / 4  # Here, (3 + 5) / 4 is the expression.
print("Expression result:", expression_result)

# 2. STATEMENTS
# Concept: A statement is a programming instruction that does something.
# It is like giving a direct order to Python, e.g., "Print this!" or "Save this value!".
# A statement executes and may or may not yield a value.
a = 15  # This entire line is a statement.
print("Hello, I am a statement!")  # This is also a statement.


print("\n--- 2. COMMENTS ---")

# Concept: Comments are additional readable information to clarify the source code.
# They are ignored by the Python interpreter.
# In Python, comments begin with symbol # (Pound or hash character).

# There are two main types of comments using the # symbol:
# 1. Full line comments: The physical lines beginning with # are the full line comments.
b = 10  # 2. Inline comment: Starts in the middle of a physical line, after Python code.

# 3. Multi-line comments / Docstrings:
# You can enter a multi-line comment in Python code by adding a # symbol in the beginning of every physical line.
# Alternatively, you can use triple-apostrophe (''') or triple quotes (""") to write docstrings.
"""
This type of multi-line comment is also known as docstring.
They are very useful in documentation.
"""


print("\n--- 3. FUNCTIONS, BLOCKS, AND INDENTATION ---")

# Concept: A function is a code that has a name and it can be reused (executed again).
# Concept: A group of statements is part of another statement or function, which is called a block or code-block or suite.
# Many languages use curly brackets to show blocks, but Python uses indentation.
# Blocks of code are denoted by line indentation, which is enforced through 4 spaces (not tabs) per indentation level.

def SeeYou():  # Defining a function
    # The statements indented below belong to this function's block.
    print("Time to say Good Bye !!") 

# Let's see a block inside an 'if' condition:
if a > 5:
    print("Value of 'a' was more than 5")  # Indented block
    
SeeYou()  # Function-call statement


print("\n--- 4. HOW VARIABLES ACTUALLY WORK IN PYTHON (MEMORY MAGIC) ---")

# VERY IMPORTANT CONCEPT FOR BEGINNERS!
# In traditional languages (like C/C++), a variable is a storage container with a fixed memory address.
# BUT PYTHON VARIABLES ARE NOT CREATED IN THE FORM MOST OTHER PROGRAMMING LANGUAGES DO.
# In Python, variables are created as labels pointing to memory locations.

age = 15 
# Python creates a memory box for '15' and sticks a label called 'age' on it.
print("Age is pointing to 15. Memory Address of 15 is:", id(age))

age = 20 
# When we change the value to 20, Python DOES NOT put 20 in the old box.
# It creates a NEW box for '20' and moves the 'age' label to this new box.
print("Age is now pointing to 20. Memory Address changed to:", id(age))
# Thus variables in Python do not have fixed locations unlike other programming languages.


print("\n--- 5. LVALUES AND RVALUES ---")

# Concept: Broadly lvalue and rvalue can be thought of as:
# lvalue: expressions that can come on the lhs (left hand side) of an assignment.
# rvalue: expressions that can come on the rhs (right hand side) of an assignment.

my_score = 100  # CORRECT: 'my_score' is an Lvalue, '100' is an Rvalue.
# 100 = my_score  # ERROR! Literals (like 100) cannot come on LHS. They are rvalues.


print("\n--- 6. MULTIPLE ASSIGNMENTS ---")

# 1. Assigning same value to multiple variables:
# You can assign same value to multiple variables in a single statement.
p = q = r = 10
print("Same values assigned:", p, q, r) # All labels point to the same location of value 10.

# 2. Assigning multiple values to multiple variables:
# It will assign the values order wise.
x, y, z = 10, 20, 30
print("Order wise assignment:", x, y, z)

# Concept: SWAPPING VALUES
# In Python, to swap values, you just write x, y = y, x.
print("Before Swapping: x =", x, "y =", y)
x, y = y, x
print("After Swapping: x =", x, "y =", y)

# HOW DOES PYTHON EVALUATE MULTIPLE ASSIGNMENTS?
# Rule: Python first evaluates the RHS (right hand side) expression(s) completely, and then assigns them to LHS.
# Let's look at a tricky example:
m = 10
n = 5
m, n = m + 2, m + 5 
# First, RHS is evaluated: m+2 becomes 12, m+5 becomes 15 (using the OLD value of m which is 10).
# Then assigned to LHS: m becomes 12, n becomes 15.
print("Tricky assignment output. m:", m, "n:", n)