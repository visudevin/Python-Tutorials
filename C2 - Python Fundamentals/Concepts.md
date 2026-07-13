# 📚 Chapter 2: Python Fundamentals

## 2.1 Introduction
*(Placeholder for introductory concepts regarding Python fundamentals.)*

---

## 2.2 Python Character Set
A character set is a set of valid characters that a language can recognize. 
- A character represents any letter, digit, or other symbol.
- Python supports the **Unicode** encoding standard, meaning it can handle characters from almost all languages in the world.

---

## 2.3 Tokens (Lexical Units)
A token is the smallest individual unit of a program (also known as a lexical unit).

### 1. Keywords
Keywords are reserved words in Python that have special meanings for the interpreter.
- They **cannot** be used as variable names, function names, or any other identifiers.
- *Examples:* `False`, `await`, `else`, `if`, `True`.

### 2. Identifiers
Identifiers are the names given to entities like variables, objects, classes, functions, and lists.
- **Rules for writing identifiers:**
  - **Any length:** The length of an identifier doesn't matter (e.g., `aaaaaaaaaaaaaaaa` is valid).
  - **Allowed characters:** Can be a combination of uppercase letters (`A` to `Z`), lowercase letters (`a` to `z`), digits (`0` to `9`), and underscores (`_`). Examples: `ABC123`, `ABC_123`.
  - **No starting digits:** Cannot start with a digit (e.g., `123xyz` is invalid, but `xyz123` is valid).
  - **No keywords:** Keywords cannot be used (e.g., `pass` is invalid because it is a keyword, but `asap` is valid).
  - **No special symbols:** Special characters like `!`, `@`, `#`, `$`, `^` are not allowed (e.g., `_under` is valid, but `!.@#$^` is invalid).

### 3. Literals / Values
Literals represent fixed values in the source code[cite: 1]. They are the raw data given to variables or constants[cite: 1].

* **String Literals:** A group of characters enclosed within quotes[cite: 1].
  - Can be enclosed in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`)[cite: 1].
  - Triple quotes are used for multi-line strings[cite: 1].
  - The size of the string counts all characters and escape sequences (e.g., `"xyz"` has size 3, `"Acer\'s Aspire5"` has size 13)[cite: 1].
* **Numeric Literals:** Immutable numerical values[cite: 1].
  - **Integer Literals:** Includes numeric decimal, binary (`0b...`), octal (`0o...`), and hexadecimal (`0x...`) integers[cite: 1].
  - **Float Literals:** Real literals that have both an integer and a fractional part (e.g., `14.5`)[cite: 1]. They can be written in Fractional form (signed or unsigned digits) or Exponent form (contains Mantissa and Exponent, e.g., `0.58E01` means $0.58 \times 10^1$)[cite: 1].
  - **Complex Literals:** Written in the form of `a+bj`, where `a` is the real part and `b` is the complex part (e.g., `7+5j`)[cite: 1].
* **Boolean Literals:** Represents `True` or `False`[cite: 1].
  - Internally, `True` behaves like `1` and `False` behaves like `0` (e.g., `True + 3` evaluates to `4`)[cite: 1].
* **Special Literal (`None`):** Defines a null variable[cite: 1].
  - `None` means there is absolutely nothing there[cite: 1]. It is not equal to `0` (because `0` is an integer value, while `None` is the absence of a value)[cite: 1]. *(Note: In Python, comparing `None == None` evaluates to `True`, not `False`).*

#### Literal Collections
* **List Literals:** Started with square brackets `[]` and entities are separated by commas[cite: 1]. They can store different types of data and are **mutable** (data can be changed)[cite: 1]. Example: `[1, 2, 3, 4, 5]` or `['Python', 'Spidey', 'Anaconda', 2]`[cite: 1].
* **Tuple Literals:** Started with parentheses `()` and entities are separated by commas[cite: 1]. They can store different types of data but are **immutable** (cannot be changed once created)[cite: 1]. Example: `(2, 4, 6, 8)`[cite: 1].
* **Dictionary Literals:** Started with curly brackets `{}`[cite: 1]. Data is stored in `key:value` pairs separated by commas[cite: 1]. They are **mutable**[cite: 1]. Example: `{'a': 'apple', 'b':'ball'}`[cite: 1].
* **Set Literals:** Started with curly brackets `{}` with entities separated by commas[cite: 1]. The data is unordered and not in key:value pairs[cite: 1]. Example: `{'a', 'e', 'i', 'u'}`[cite: 1].

---

### 4. Operators
Operators are used to perform operations on operands (variables and values)[cite: 1].

* **Arithmetic Operators:**
  - `+` (Addition), `-` (Subtraction), `*` (Multiplication)[cite: 1].
  - `/` (Division): Divides and gives a real float value, unlike C/C++[cite: 1].
  - `%` (Modulus): Gives the remainder[cite: 1].
  - `**` (Exponentiation): Calculates the power[cite: 1].
  - `//` (Floor Division): Gives the integer quotient[cite: 1].
* **Relational / Comparison Operators:** Returns either `True` or `False`[cite: 1].
  - `==` (Equal to), `!=` (Not equal to)[cite: 1].
  - `>`, `<`, `>=`, `<=`[cite: 1].
* **Identity Operators:** Used for comparing objects' memory locations[cite: 1].
  - `is`: Returns `True` if variables have the same object in them (i.e., they share the exact same memory address/home)[cite: 1].
  - `is not`: Returns `True` if variables do not share the same object/memory address[cite: 1].
  - *Difference from `==`:* `==` checks if the items inside the houses are the same, while `is` checks if it is literally the same house[cite: 1].
* **Assignment Operators:** Used to assign values to variables[cite: 1].
  - `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=`, `**=`[cite: 1]. (Example: `x += 3` is the same as `x = x + 3`)[cite: 1].
* **Membership Operators:** Used to test if a sequence is present in an object[cite: 1].
  - `in`: Returns `True` if the specified value is present[cite: 1].
  - `not in`: Returns `True` if the specified value is not present[cite: 1].

#### 🧠 Concept Check: Logical vs. Bitwise Operators

**Logical Operators (`and`, `or`, `not`)**[cite: 1]:
- **What they do:** They evaluate entire conditions and return Boolean results (`True` or `False`).
- **Use case:** Used in decision-making (like `if` statements).
- **Rules:**
  - `and`: Returns `True` only if *both* conditions are `True`[cite: 1].
  - `or`: Returns `True` if *at least one* condition is `True`[cite: 1].
  - `not`: Inverts the Boolean result[cite: 1].

**Bitwise Operators (`&`, `|`, `^`, `~`, `<<`, `>>`)**[cite: 1]:
- **What they do:** They convert numbers into binary (1s and 0s) and compare them *bit by bit* rather than evaluating boolean conditions[cite: 1].
- **Use case:** Used in low-level programming and cryptography.
- **Rules:**
  - `&` (AND): Sets the bit to `1` if *both* bits are `1`, otherwise `0`[cite: 1].
  - `|` (OR): Sets the bit to `1` if *at least one* bit is `1`[cite: 1].
  - `^` (XOR): Sets the bit to `1` only if the bits are *different* (one is `1`, the other is `0`)[cite: 1].
  - `~` (NOT): Inverts all bits (turns `1` to `0`, and `0` to `1`)[cite: 1].
  - `<<` (Left Shift): Shifts bits to the left, removing bits from the left and filling with zeros on the right side[cite: 1].
  - `>>` (Right Shift): Shifts bits to the right, removing bits from the right side and filling with zeros on the left side[cite: 1].

### 5. Punctuators
*(Placeholder for symbols used in syntax, e.g., commas, colons, parentheses).*

---

## 2.4 Barebones of a Python Program
*(Placeholder for program structure details).*

---

## 2.5 Variables and Assignments
- **Creating a Variable:** Reserving memory space to store a value.
- **Multiple Assignments:** Assigning values to multiple variables in a single line (e.g., `a, b = 10, 20`).
- **Variable Definition:** The moment a variable is assigned a value.
- **Dynamic Typing:** Python automatically determines the data type based on the value assigned. A variable can change its type during execution (e.g., `x = 5`, then `x = "Hello"`).

---

## 2.6 Simple Input and Output
- **Reading Numbers:** Utilizing the `input()` function combined with `int()` or `float()` to get numeric data from the user.
- **Output through print function:** Utilizing `print()` to display output to the screen, which can handle strings, variables, and expressions.