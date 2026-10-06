# 🎯 Number Guessing Game

A simple Python game where the computer chooses a random number between **1 and 30**, and the player tries to guess it.

## 📌 How It Works

1. The computer generates a random number from **1 to 30**.
2. The player enters a guess.
3. The program checks the guess:

   * If the guess is **too low**, it says `Too low!`
   * If the guess is **too high**, it says `Too high!`
   * If the guess is **correct**, the game congratulates the player.
4. The game continues until the correct number is guessed.

---

## 💻 Code

```python
import random

number = random.randint(1, 30)

while True:
    guess = int(input("Guess the number (1-30): "))

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
        break
```

---

## 🔍 Code Explanation

### 1. Importing `random`

```python
import random
```

`random` is a Python module that allows us to generate random values.

We use it because we want the computer to choose a secret number randomly.

---

### 2. Generating the Secret Number

```python
number = random.randint(1, 30)
```

`randint(1, 30)` generates a random **integer** between `1` and `30`.

Both `1` and `30` are included.

For example, Python might generate:

```text
17
```

The number is stored inside the variable `number`.

---

### 3. Creating the Loop

```python
while True:
```

This creates a loop that continues running.

The player can therefore make multiple guesses.

The loop will continue until we use:

```python
break
```

---

### 4. Getting the Player's Guess

```python
guess = int(input("Guess the number (1-30): "))
```

There are three important parts here:

**`input()`**

Gets information from the user.

**`int()`**

Converts the user's input from a string into an integer.

**`guess =`**

Stores the converted number in the variable `guess`.

For example:

```text
Guess the number (1-30): 15
```

Now:

```python
guess = 15
```

---

### 5. Checking If the Guess Is Too Low

```python
if guess < number:
```

`<` means **less than**.

The program asks:

> Is the player's guess smaller than the secret number?

For example:

```text
Secret number = 20
Guess = 10
```

Python checks:

```python
10 < 20
```

This is `True`, so it displays:

```text
Too low! Try again.
```

---

### 6. Checking If the Guess Is Too High

```python
elif guess > number:
```

`>` means **greater than**.

The program asks:

> Is the player's guess greater than the secret number?

For example:

```text
Secret number = 20
Guess = 25
```

Python checks:

```python
25 > 20
```

This is `True`, so it displays:

```text
Too high! Try again.
```

---

### 7. Correct Guess

```python
else:
    print("🎉 Correct! You guessed the number.")
```

If the guess is neither lower nor higher, it must be equal to the secret number.

For example:

```text
Secret number = 20
Guess = 20
```

The program prints:

```text
🎉 Correct! You guessed the number.
```

---

### 8. Stopping the Game

```python
break
```

`break` stops the `while` loop.

Without `break`, the game would continue asking for guesses even after the player found the correct number.

---

## ▶️ Example Output

```text
Guess the number (1-30): 10
Too low! Try again.

Guess the number (1-30): 25
Too high! Try again.

Guess the number (1-30): 18
Too low! Try again.

Guess the number (1-30): 21
🎉 Correct! You guessed the number.
```

---

## 🧠 Concepts Used

This project teaches:

* `import`
* Modules
* Variables
* `random.randint()`
* `input()`
* `int()`
* `while` loops
* `if`
* `elif`
* `else`
* Comparison operators
* `print()`
* `break`

## 🚀 Future Improvements

You can make this game more advanced by adding:

* Input validation
* A limited number of attempts
* A score system
* Difficulty levels
* A play-again option
* Hints
* Error handling with `try` and `except`

## 🎓 What You Learn From This Project

The main idea is:

```text
Generate Number
      ↓
Ask for Guess
      ↓
Compare Guess
      ↓
Too Low / Too High / Correct
      ↓
If Wrong → Guess Again
      ↓
If Correct → Stop
```

This project is a great way to practice **variables, conditions, loops, input, and random numbers** in Python.
