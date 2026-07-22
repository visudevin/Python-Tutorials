# ==========================================
# CodeWithHarry - Program 11 (For Loops, Unpacking & Logic)
# File: p11.py
# ==========================================

# ------------------------------------------
# 1. Unpacking Lists and Dictionaries
# ------------------------------------------
list1 = [['harry', 1], ['larry', 2], ['carry', 6], ['marie', 250]]

# Unpacking with the help of a list
print("--- Unpacking List ---")
for falna, dhimkana in list1:
    print(falna, "and lollypop is", dhimkana)

# Converting list to dictionary
dict1 = dict(list1)
print("\n--- Unpacking Dictionary ---")

# Unpacking with the help of dict (using .items())
for item, lollypop in dict1.items():
    print(item, "and lollypop is", lollypop)

print("\n--- Iterating over Dict Keys and Values ---")
# Iterating over keys
for item in dict1:
    print("Key:", item)

# Iterating over values
for lollypop in dict1.values():
    print("Value:", lollypop)


# ------------------------------------------
# 2. Filtering a Mixed List
# ------------------------------------------
print("\n--- Filtering Mixed List ---")
# Exercise: Print items that are numeric AND greater than 6
list3 = [int, 23, 'yeah', 'no', 60, 8, 9, 3, 2, 1]

for falana in list3:
    # str(falana).isnumeric() checks if it's a number safely.
    # If False, it short-circuits and skips the > 6 check, preventing crashes!
    if str(falana).isnumeric() and falana > 6:
        print(falana, "is a Number Greater Than 6")