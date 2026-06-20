# Random Password Generator in Python

A Python-based random password generator that creates secure passwords using letters, digits, and symbols. It includes input validation, minimum password length checks, and a simple interactive command-line interface.

## Features
- Generates random secure passwords
- Uses:
  - Uppercase and lowercase letters
  - Numbers
  - Special symbols
- Input validation with error handling
- Minimum length security warning for passwords shorter than 8 characters
- Exit option for ending the program

## Technologies Used
- Python
- `random` module
- `string` module

## How It Works
1. The user enters the desired password length.
2. If the input is not a valid number, the program shows an error.
3. If the password length is less than 8, the program displays a security warning.
4. The program combines letters, digits, and symbols into one character pool.
5. A random password is generated from that pool and displayed to the user.

## Python Code
```python
import random
import string

print("=== WELCOME TO DECODELABS SECURITY PHASE ===")
print("Project 3: Random Password Generator Engine\n")

while True:
    user_input = input("Enter the desired password length (or type 'exit' to stop): ").strip()
    
    if user_input.lower() == 'exit':
        print("\nExiting the Security Engine. Milestone 3 Qualified! Powered by DecodeLabs.")
        break
        
    try:
        length = int(user_input)
        
        if length < 8:
            print("Security Warning: Passwords shorter than 8 characters are insecure! Try 12+.")
            continue
            
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation
        
        all_characters = letters + digits + symbols
        password_list = random.choices(all_characters, k=length)
        password = "".join(password_list)
        
        print(f"\nGenerated Secure Password: {password}")
        print("-" * 40)
        
    except ValueError:
        print("Invalid Input: Please enter a valid number for length!")
        print("-" * 40)
