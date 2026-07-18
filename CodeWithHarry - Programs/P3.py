# ==========================================
# CodeWithHarry - Program 3 (String Slicing & Methods)
# File: p3.py
# ==========================================

hell = "Visu is a Ambivert Guy"
hell2 = "VisuisaAmbivertGuy"
hell3 = "Visu is a Ambivert Guy"

print("Length of string:", len(hell))
print("Character at index 3:", hell[3])

# ------------------------------------------
# String Slicing [Start : Stop : Step]
# ------------------------------------------
print("\n--- Slicing Examples ---")
print(hell[0:6])

print(hell[0:22:2])   # Step is 2: Take every 2nd character (skips 1)
print(hell[0:22:3])   # Step is 3: Take every 3rd character (skips 2)
print(hell[0:22:555]) # Step is way too large: Just prints the first character

# Resolving the Step 1 Doubt:
print(hell[0:4:1]) # Step is 1: Means move normally one-by-one (no skipping).
print(hell[0:4:2]) # Step is 2: Means move two steps at a time (skips 1).

print(hell[:4])    # By default, start is 0
print(hell[:])     # By default, start is 0 and stop is end of string
print(hell[::])    # Same as hell[0:22:1]

# ------------------------------------------
# Reverse Slicing (Negative Steps)
# ------------------------------------------
print("\n--- Reverse Slicing ---")
print(hell[18:22]) 

# Note: The next two lines will print NOTHING (empty string).
# Reason: You can't go forward from 18 to 22 while stepping backwards (-1).
print("Incorrect reverse:", hell[18:22:-1]) 
print("Incorrect reverse 2:", hell[18:22:-2]) 

# Correct way to reverse a specific part: Start must be greater than Stop
print("Correct reverse part:", hell[21:17:-1]) 

print(hell[-4:-2]) # Using negative indices
print(hell[18:20]) 

# Reversing the whole string
print("Full Reverse:", hell[::-1]) 
print("Full Reverse with skip:", hell[::-2]) 

# ------------------------------------------
# String Methods
# ------------------------------------------
print("\n--- String Methods ---")

# isalnum(): True if all characters are alphanumeric (No spaces allowed)
print("Is 'hell' alphanumeric?", hell.isalnum())   # False (Has spaces)
print("Is 'hell2' alphanumeric?", hell2.isalnum()) # True

# isalpha(): True if all characters are alphabets (No numbers, no spaces)
print("Is 'hell2' alphabetic?", hell2.isalpha())   # True
print("Is 'hell3' alphabetic?", hell3.isalpha())   # False (Has spaces)

print("\n--- endswith() ---")
print(hell2.endswith("boy"))  # False
print(hell2.endswith("bdoy")) # False
print(hell.endswith("Guy"))   # Changed 'boy' to 'Guy' to show a True example
print(hell.endswith("bdoy"))  # False

print("\n--- Formatting & Searching ---")
# capitalize(): Capitalizes first letter of the string, makes the rest small
print(hell.capitalize()) 

print("Count of 'i':", hell.count("i"))

# find(): Returns the starting index of the word/character. If not found, returns -1
print("Index of 'is':", hell.find("is"))

print("Lowercase:", hell.lower())
print("Replace:", hell.replace("is", "areee"))