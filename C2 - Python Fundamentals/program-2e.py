# ==========================================
# Chapter 2: Advanced I/O & Practical Programs
# File: program-2e.py
# ==========================================

print("--- 1. READING NUMBERS & THE TYPECASTING TRAP ---")

# Concept: input() function hamesha ek 'string' return karta hai.
# Agar hume math (arithmetic) karni hai, toh hume string values ko numbers (int ya float) mein badalna padta hai.
# Python iske liye do functions deta hai: int() aur float().

# Humn isko ek hi step mein combine kar sakte hain:
# Example (Uncomment to test):
# age = int(input("Enter your age: "))

# 🚨 THE CRASH TRAP (Possible Errors)
# Agar aapne code mein int() lagaya hai, aur user ne '17.5' (decimal) daal diya, 
# toh Python turant 'ValueError' de dega. 
# Rule: Jo value enter ho rahi hai, wo 'int' ke compatible honi chahiye.

# Lekin agar aap float() use karte ho, toh wo 73 (integer) ko bhi easily 73.0 mein convert kar lega bina kisi error ke.
print("Tip: If you are expecting decimals, ALWAYS use float() instead of int() to avoid ValueError!")


print("\n--- 2. THE SECRETS OF print() STATEMENT ---")

# Concept: print() function humari values ko screen par dikhata hai, par iske 2 chhote secrets hain!
# 1. Ye automatically saare items ko string mein convert karke print karta hai.
# 2. Ye items ke beech mein khud-ba-khud 'space' daal deta hai.

# Secret 1: 'sep' argument (Separator)
# By default, sep ki value space (' ') hoti hai.
print("My", "name", "is", "Python")  # Output: My name is Python

# Hum is 'sep' ko apne hisaab se badal sakte hain!
print("My", "name", "is", "Python", sep="...")  # Output: My...name...is...Python

# Secret 2: 'end' argument
# By default, print() apna kaam khatam karne ke baad ek nayi line (newline '\n') daal deta hai.
# Hum isko rok sakte hain aur line ke aakhir mein kuch aur laga sakte hain.
print("Hello", end=" -> ")
print("World!")  
# Output will be on the SAME line: Hello -> World!


print("\n--- 3. PRACTICAL PROGRAMS (Let's build something!) ---")

# Program A: Rectangle Area Calculator
# Concept: Length aur breadth float mein lena better hai kyunki measurements decimal mein ho sakti hain.
print("-> Rectangle Area Calculator")
length = 8.75  # Man lo user ne enter kiya: float(input("Enter length: "))
breadth = 35.0
area = length * breadth
print("Length =", length, "Breadth =", breadth)
print("Area =", area)

# Program B: BMI (Body Mass Index) Calculator
# Formula: BMI = weight (kg) / height^2 (meters)
print("\n-> BMI Calculator")
weight_in_kg = 66.0
height_in_meter = 1.6
bmi = weight_in_kg / (height_in_meter * height_in_meter)
print("Weight:", weight_in_kg, "kg | Height:", height_in_meter, "m")
print("BMI is:", bmi)


print("\n--- 4. QUICK REVISION (Keywords vs Identifiers) ---")

# Concept:
# KEYWORDS: Ye reserved words hote hain jinka ek special meaning hota hai (jaise if, elif, else). Aap inko variable ka naam nahi bana sakte.
# IDENTIFIERS: Ye user (coder) ke dwara diye gaye naam hote hain (jaise variables, functions ke naam). 
# Rule: Identifier hamesha letter (A-Z, a-z) ya underscore (_) se shuru hona chahiye, numbers se nahi!

print("Revision complete! We are now masters of basic I/O in Python.")
