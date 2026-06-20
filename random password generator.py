# DecodeLabs - Python Project 3: Random Password Generator
import random
import string

print("=== WELCOME TO DECODELABS SECURITY PHASE ===")
print("Project 3: Random Password Generator Engine\n")

while True:
    user_input = input("Enter the desired password length (or type 'exit' to stop): ").strip()
    
    if user_input.lower() == 'exit':
        print("\nExiting the Security Engine. Milestone 3 Qualified! Powered by DecodeLabs.")
        break
        
    # Digital Poka-Yoke: Error handling for input validation
    try:
        length = int(user_input)
        
        # NIST Guidelines: Suggesting safe password length
        if length < 8:
            print("Security Warning: Passwords shorter than 8 characters are insecure! Try 12+.")
            continue
            
        # 1. POOLING CHARACTER SETS: Gathering the raw materials
        letters = string.ascii_letters  # Contains both lowercase and uppercase (a-z, A-Z)
        digits = string.digits          # Contains numbers (0-9)
        symbols = string.punctuation    # Contains symbols (!, @, #, $, etc.)
        
        # Combining all characters into one pool
        all_characters = letters + digits + symbols
        
        # 2. SELECTION ALGORITHM: Generating random password
        # random.choices() picks random characters from the pool 'length' number of times
        password_list = random.choices(all_characters, k=length)
        
        # Transforming the list back into a single string
        password = "".join(password_list)
        
        print(f"\nGenerated Secure Password: {password}")
        print("-" * 40)
        
    except ValueError:
        print("Invalid Input: Please enter a valid number for length!")
        print("-" * 40)