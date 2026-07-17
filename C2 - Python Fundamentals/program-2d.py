# ==========================================
# Chapter 2: Style Rules, Dynamic Typing & Input Traps
# File: program-2d.py
# ==========================================

print("--- 1. PYTHON STYLE RULES & CONVENTIONS ---")

# Concept: Jab hum Python code likhte hain, toh kuch standard rules follow karne hote hain taaki code saaf aur sahi dikhe.
# 1. Statement Termination: Python mein line khatam karne ke liye koi symbol (jaise semicolon ;) zaroori nahi hota. Bas 'Enter' key dabao, statement terminate ho jayega.
# 2. Maximum Line Length: Ek line mein zyada se zyada 79 characters hone chahiye.
# 3. Lines and Indentation: Blocks ko alag dikhane ke liye 4 spaces (tabs nahi) ka indentation zaroori hai.
# 4. Case Sensitive: Python case sensitive hai (Yani 'A' aur 'a' dono alag mane jate hain). 

variable_a = 5
Variable_A = 10
print("Case Sensitivity Check:", variable_a, "is different from", Variable_A)


print("\n--- 2. VARIABLE DEFINITION (The Creation Rule) ---")

# Concept: Python mein variable tab tak "create" nahi hota, jab tak aap usme koi value assign na karein.
# Agar aap kisi aisi cheez ko print karne ki koshish karoge jisme value dali hi nahi, toh Python 'NameError' de dega.

# 🚨 UNCOMMENT THE BELOW LINE TO SEE THE ERROR:
# print(magic_box)  
# Python will cry: "NameError: name 'magic_box' is not defined".

# Sahi tareeka (Pehle value assign karo):
magic_box = 100  # Variable is officially created now!
print("Magic Box is now defined:", magic_box)


print("\n--- 3. DYNAMIC TYPING ---")

# Concept: In Python, a variable is defined by assigning to it some value. 
# Variable ka apna koi data type nahi hota; type us value se attach hota hai jisko variable point kar raha hai.
# Aap ek hi variable ka type program chalte waqt badal sakte ho bina kisi error ke. Ise 'Dynamic Typing' kehte hain.

x = 10  # Label 'x' is pointing to an Integer
print("x holds an integer:", x)

x = "Hello World" # Now 'x' drops the integer and points to a String
print("x now holds a string:", x)

# 🚨 CAUTION WITH DYNAMIC TYPING
# Programmer ko khud dhyaan rakhna padta hai ki variable ke andar abhi kya type pada hai.
# Agar string ko divide karne ki koshish ki, toh error aayega!
# Example: x = 'Day' -> x / 2 karega toh ERROR aayega kyunki string divide nahi hoti.

# Aap type() function ka use karke kisi bhi variable ka current type check kar sakte ho:
test_var = 20.5
print("What is the type of test_var (20.5)? ->", type(test_var))


print("\n--- 4. SIMPLE INPUT AND THE STRING TRAP ---")

# Concept: Python 3.x mein user se data lene ke liye built-in function input() use hota hai.
# 🚨 THE BIGGEST TRAP: The input() function ALWAYS returns a value of String type!

# Agar user numbers (jaise 16) bhi daale, tab bhi input() usko "16" (string) ki tarah read karta hai.
# Is wajah se aap direct input li hui age mein math (e.g., age + 1) nahi laga sakte, 'TypeError' aayega.

# Note: In lines ko mobile/VS code terminal mein test karne ke liye uncomment kar lena:
'''
print("Reading string input:")
name = input("What is your name? ") 
print("Welcome,", name)

print("\nThe String Trap in Numbers:")
raw_age = input("Enter your age: ")  # User types 16
print("Type of raw_age is:", type(raw_age)) # Output will show it is a <class 'str'>!
# print(raw_age + 1)  # THIS WILL CRASH! (TypeError: must be str, not int).
'''

print("\n--- 5. READING NUMBERS SAFELY ---")

# Solution: String values cannot be used for arithmetic operations. 
# Hamein input() ki values ko numbers mein convert (typecast) karna padta hai.
# Python offers two functions int() and float() to convert string type into numeric types.

# Sahi Tareeka:
'''
safe_age = int(input("Enter your age safely: ")) # int() string '16' ko math wale 16 mein badal dega
print("In 5 years, you will be:", safe_age + 5) # Now this works perfectly!
'''
