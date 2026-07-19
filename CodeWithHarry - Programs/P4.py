# ==========================================
# CodeWithHarry - Program 4 (Lists & Slicing)
# File: p4.py
# ==========================================

# ------------------------------------------
# 1. Basic Lists
# ------------------------------------------
grocery = ["iron man suit", "mjolnir", "stark industries", 56]
print("Grocery List:", grocery)
print("Item at index 1:", grocery[1])
print("Item at index 3:", grocery[3])

numbers = [2, 7, 9, 11, 3]
print("\nOriginal Numbers:", numbers)
print("Number at index 2:", numbers[2])

# ------------------------------------------
# 2. List Methods (Modifies Original List)
# ------------------------------------------
# Functions like sort() and reverse() change the ORIGINAL list permanently.
# numbers.sort()
# numbers.reverse()
print("Numbers after sort/reverse (commented out):", numbers)

# ------------------------------------------
# 3. List Slicing [Start : Stop : Step]
# ------------------------------------------
# Slicing doesn't change the original list. 
# Iska kaam bas list se values ko chhant kar (filter karke) naya result show karna hai.
print("\n--- Positive Slicing ---")
print(numbers[0:4])
print(numbers[:])       # Full list
print(numbers[0:])      # From 0 to end
print(numbers[:5])      # From start to index 4
print(numbers[1:])      # From index 1 to end
print(numbers[1:5])     
print(numbers[1:4])
print(numbers[::1])     # Normal list (step 1)
print(numbers[::2])     # Skip 1 element (step 2)
print(numbers[::3])     # Skip 2 elements (step 3)

# ------------------------------------------
# Reverse Slicing (Negative Steps)
# ------------------------------------------
print("\n--- Negative Slicing ---")
print("Current numbers:", numbers)
print(numbers[5::-1])   # Reverse list
print(numbers[5::-2])   # Reverse with step 2
print(numbers[5:1:-1])  # Reverse from end down to index 2
print(numbers[5:1:-2])  
print(numbers[5::-3])   

# ------------------------------------------
# 4. List Functions
# ------------------------------------------
print("\n--- List Functions ---")
print("Max value:", max(numbers))
print("Total items (length):", len(numbers))
print("Min value:", min(numbers))

# ------------------------------------------
# 5. Modifying Lists (Adding/Removing)
# ------------------------------------------
numbers.append(71)       # Append adds numbers or value to the very end of the list
numbers.append(71)
numbers.insert(1, 45)    # Insert 45 at index 1
numbers.remove(11)       # Removes the first occurrence of 11
# numbers.pop()          # Removes the last element of the list

print("\nye raha result:", numbers)

# ------------------------------------------
# 6. Mutability (Changing specific index)
# ------------------------------------------
numbers[2] = 98          # Value change ho raha hai list ke andar
print("After changing index 2 to 98:", numbers)

#value in tuple not change 
#only value change in list 

