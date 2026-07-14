# ==========================================
# Chapter 2: String Literals & EOL Concepts
# File: program-2a.py
# ==========================================

# ------------------------------------------
# 1. Single Line Strings & Syntax Errors
# ------------------------------------------
print("--- Single Line Strings ---")

# Normal single line string using single quotes.
# If you press 'Enter' inside a single or double quote, Python throws a Syntax Error.
# Example of what NOT to do (Uncommenting the below lines will cause an error):
# text1 = 'hello 
# there'
# print(text1) 


# ------------------------------------------
# 2. Line Continuation using Backslash (\)
# ------------------------------------------
# Adding a backslash (\) at the end of a line inside single/double quotes 
# allows you to continue writing code on the next line in your editor.
# However, it prints as a single continuous line in the output.
text2 = 'hello \
world' 
print("Text 2 Output:", text2)


# ------------------------------------------
# 3. True Multiline Strings (Triple Quotes)
# ------------------------------------------
print("\n--- Multiline Strings ---")

# Multiline strings can be created using triple single quotes (''') or triple double quotes (""").
# It preserves the exact formatting, including spaces and line breaks.

text3 = '''
Hello 
Everyone 
Whats Up?
'''
print("Text 3 Output:", text3)

text4 = """
Mikasa 
Eren
Ethen Hunt
"""
print("Text 4 Output:", text4)


# ------------------------------------------
# 4. String Size & EOL (End of Line) Characters
# ------------------------------------------
print("\n--- String Size and EOL Characters ---")

# In standard triple quotes, every time you press 'Enter', a hidden EOL character (\n) is added.
# This hidden character is counted in the total length of the string.
str3 = '''a
b
c 
'''
print("Output of str3:")
print(str3)
print("Length of str3 (EOL is counted):", len(str3))

# If you use a backslash (\) at the end of a line in a multiline string, 
# it ignores the 'Enter' (EOL character). Therefore, the EOL is NOT counted in the string's length.
str4 = '''a\
b\
c 
'''
print("Output of str4:")
print(str4)
print("Length of str4 (EOL is NOT counted):", len(str4))