# ==========================================
# CodeWithHarry - Program 2 (Variables & Typecasting)
# File: p2.py
# ==========================================

var = "54"
var4 = "32"
var2 = 2
var3  = 35.5

# Basic printing
print(var)

# String Concatenation ("54" + "32" = "5432")
print(var + var4)

# Typecasting: Converting strings to int, adding them, then converting back to string to multiply
print(10 * str(int(var) + int(var4))) 

# Type of literals
print(type(var)) 

# String multiplication
print(3 * "hellovisu " * 2)

# ------------------------------------------
# Practice Inputs (Currently commented out)
# ------------------------------------------
"""
print("Enter your number")
inpnum = input()
print("You entered the number", inpnum+"ding")

print("Enter your number")
inpnum = input()
print("You entered the number", int(inpnum)+10)

print("Enter your number")
inpnum = input()
print("You entered the number", inpnum)
"""

# ------------------------------------------
# Basic Calculator using Input & Typecasting
# ------------------------------------------
print("Enter First Number")
varo = input()
print("Enter Second Number")
vart = input()

# Typecasting inputs from string to integer before adding
print(int(varo) + int(vart))