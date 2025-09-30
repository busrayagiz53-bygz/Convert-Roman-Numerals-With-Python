"""
# Introduction
Roman numerals originated, as the name suggests, in ancient Rome more than 2,800 years ago. After the Romans’ eventual demise, numerals were still widely used during the Middle Ages. Even today, Roman numerals are prevalent in our everyday lives, showing up in clocks, movie titles, and more!

Instead of numbers like 1 and 2, Roman numerals use letters (predominantly "I" and "V").

Using the chart above, "I" is 1, "V" is 5, "X" is 10, and so on…

However, when a large combination of these values gets thrown together, the value of the numeral becomes difficult to read.

Luckily, a sequence of Roman numerals can be easily converted to numbers with Python!

In this tutorial, we will be using loops, control flow statements, and built-in Python functions to convert any Roman numeral into a number. Let’s jump in!

# Setup
You'll need an editor for this tutorial. This can be achieved with any of the following:

You can write the code in our built-in Python editor.
You can save and run the code from a separate roman_numeral.py file in an editor of your choice (we recommend VS Code).
After setting up, feel free to move onward!
"""

roman_int = input("Enter the roman numerals you want to convert: ")  # Step 1: Get User Input

def roman_to_int(numeral):  # Step 2: Define roman_to_int() Function
  final_answer = 0

  if "CM" in numeral:  # Step 3: Handle Edge Cases
    final_answer += 900
    numeral = numeral.replace("CM", "")
  if "CD" in numeral:
    final_answer += 400
    numeral = numeral.replace("CD", "")
  if "XC" in numeral:
    final_answer += 90
    numeral = numeral.replace("XC", "")
  if "XL" in numeral:
    final_answer += 40
    numeral = numeral.replace("XL", "")
  if "IX" in numeral:
    final_answer += 9
    numeral = numeral.replace("IX", "")
  if "IV" in numeral:
    final_answer += 4
    numeral = numeral.replace("IV", "")

  for i in numeral:
    if i == "M":
      final_answer += 1000
    elif i == "D":
      final_answer += 500
    elif i == "C":
      final_answer += 100
    elif i == "L":
      final_answer += 50
    elif i == "X":
      final_answer += 10
    elif i == "V":
      final_answer += 5
    elif i == "I":
      final_answer += 1

  print("The roman numerals you entered translates to: " + str(final_answer) + "!")

roman_to_int(roman_int)
