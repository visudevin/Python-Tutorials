# ==========================================
# CodeWithHarry - Program 8 (Sets & Set Operations)
# File: p8.py
# ==========================================

# ------------------------------------------
# 1. Creating a Set
# ------------------------------------------
s = set()
print("Type of s:", type(s))

# Converting a List to a Set (Kept commented as original)
# l = [1, 2, 3, 4]
# sfromlist = set(l)
# print(sfromlist)
# print(type(sfromlist))

# ------------------------------------------
# 2. Adding Elements (The Unique Rule)
# ------------------------------------------
s.add(1)
s.add(2)
s.add(2) # Sets only take unique values, so the second '2' will be ignored!
print("\nSet 's' after adding elements:", s)

# ------------------------------------------
# 3. Set Operations (Union & Intersection)
# ------------------------------------------
# Union: Combines all unique elements from both sets
s1 = s.union({1, 2, 3, 4})

# Intersection: Keeps ONLY the common elements between both sets
s2 = s.intersection({1, 2, 3, 4})

print("\nUnion (s1):", s1)
print("Intersection (s2):", s2)

# ------------------------------------------
# 4. Disjoint Sets & Removing Elements
# ------------------------------------------
s4 = {4, 2}

# isdisjoint() returns True if the two sets have NO elements in common at all.
s3 = s.isdisjoint(s4) 

# Removing an element from the set
s.remove(2)

print("\nSet 's' after removing 2:", s)
print("Are 's' and 's4' disjoint? (No common elements?):", s3)

# ------------------------------------------
# 5. Built-in Functions for Sets
# ------------------------------------------
print("\n--- Set Functions ---")
# Using s1 for these functions to show better results
print("Total elements (length) in s1:", len(s1))
print("Maximum value in s1:", max(s1))
print("Minimum value in s1:", min(s1))