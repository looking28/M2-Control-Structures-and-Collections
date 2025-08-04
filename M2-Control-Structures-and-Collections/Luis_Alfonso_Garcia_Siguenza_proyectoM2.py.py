# Function that evaluates the length of an entered word
def word_length(word):
    length = len(word)

    if 4 <= length <= 8:
        print("The word is correct.")
    elif length < 4:
        print(f"Letters are missing. It only has {length} letters.")
    else:
        print(f"Too many letters. It has {length} letters.")

# Ask the user to enter a word
entered_word = input("Enter a word: ").strip()

# Check that the word is not empty
if entered_word == "":
    print("Error: You did not enter a valid word.")
else:
    word_length(entered_word)


# Function that determines in which quadrant a point (x, y) is located
def determine_quadrant(x, y):
    if x > 0 and y > 0:
        return "I"
    elif x < 0 and y > 0:
        return "II"
    elif x < 0 and y < 0:
        return "III"
    elif x > 0 and y < 0:
        return "IV"
    else:
        return "It is not located in any quadrant."

# Error handling when entering coordinates
try:
    x = float(input("Enter X: "))
    y = float(input("Enter Y: "))

    if x != 0 and y != 0:
        quadrant = determine_quadrant(x, y)
        print(f"The point is located in quadrant {quadrant}.")
    else:
        print("Please enter coordinates different from 0 for both X and Y.")
except ValueError:
    print("Error: Please enter valid numeric values for X and Y.")
