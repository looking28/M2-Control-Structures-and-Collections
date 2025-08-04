# M2-Control-Structures-and-Collections

# Word and Coordinates Evaluator

This Python program performs two main functions:

1. **Evaluates the length of a word entered by the user.**
2. **Determines which quadrant of the Cartesian plane a point lies in, based on its coordinates (X, Y).**

---

## Program Structure

The code is divided into two main sections:

---

### 1. Word Length Verification

#### Function used:

```python
def word_length(word):
```

#### Logic:

* If the word has between **4 and 8 letters**, it is considered **correct**.
* If it has **fewer than 4 letters**, it indicates that **letters are missing**.
* If it has **more than 8 letters**, it reports that there are **too many letters**.
* If the user doesn't enter anything (an empty string), an error message is displayed.

#### Input:

It asks the user for a word using `input()`.

---

### 2. Quadrant Determination

#### Function used:

```python
def determine_quadrant(x, y):
```

#### Logic:

* Quadrant I: x > 0 and y > 0
* Quadrant II: x < 0 and y > 0
* Quadrant III: x < 0 and y < 0
* Quadrant IV: x > 0 and y < 0
* If **x or y is zero**, the point **is not located in any quadrant**.

#### Input:

The program asks for two numerical values (floats) using `input()`, one for **X** and one for **Y**.

#### Error Handling:

* A `try-except` block is used to catch errors if the user does not enter valid numeric values.

---

## Development Reflections

* **Validation**: Input validation was essential to prevent runtime errors, such as empty strings or non-numeric values.
* **Conditional Logic**: This task reinforces the use of `if-elif-else` structures, which are crucial in decision-making.
* **Testing**: Various edge cases (empty input, zeros, non-numeric entries) were tested to ensure the program is robust.
* **Maintainability**: The code is modular and organized in reusable functions, which makes it easier to maintain and expand in the future.

---

## How to Run the Program

1. Make sure you have Python installed (version 3.x).
2. Copy the code into a file named `evaluador.py`.
3. Run the program in your terminal or command line:

```bash
python evaluador.py
```
