# ==========================================
# CodeWithHarry - Program 7 (Dictionary Translator)
# File: p7.py
# ==========================================

# Exercise: Create a dictionary and take input from the user 
# and return the meaning of the word from the dictionary.

# ------------------------------------------
# 1. Defining the Dictionary
# ------------------------------------------
dic = {
    "Morning": "Subah", 
    "Evening": "Shaam", 
    "Afternoon": "Dophar", 
    "Night": "Raat"
}

# ------------------------------------------
# 2. Taking User Input
# ------------------------------------------
print("--- English to Hindi Translator ---")
print("Available words: Morning, Evening, Afternoon, Night")
print("Type your word (Note: First letter must be Capital):")

user = input()

# ------------------------------------------
# 3. Output the Result
# ------------------------------------------
# This will fetch the value associated with the key entered by the user
print("Meaning:", dic[user])

# Testing a direct key fetch
print("Direct check for 'Evening':", dic["Evening"])