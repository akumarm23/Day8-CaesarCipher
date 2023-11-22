# Caesar Cipher Code Version 1.0
from logo import logo

# ASCII art logo is imported from the 'logo' module
print(logo)

# The alphabet list includes both lowercase and a repeating set of lowercase letters to handle shifts
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to perform the Caesar Cipher
def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ""
    
    # Adjust shift amount for decoding
    if cipher_direction == 'decode':
        shift_amount *= -1
    
    # Loop through each character in the input text
    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, keep it unchanged
            end_text += char
    
    # Print the result
    print(f"The {cipher_direction}d text is {end_text}")

# Variable to control the continuation of the program
should_continue = True

# Main loop
while should_continue:
    # User input for the direction ('encode' or 'decode')
    direction = input("Type 'encode' or 'decode: \n").lower()
    
    # User input for the message to be encoded or decoded
    text = input("Type your Message: \n").lower()
    
    # User input for the Caesar-Cipher SHIFT number
    shift = int(input("Type the Caesar-Cipher SHIFT number: \n"))
    
    # Ensure the shift is within the range of the alphabet
    shift %= 26
    
    # Call the Caesar Cipher function
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask the user if they want to continue
    result = input("Type 'yes' to continue; Else type 'no': \n").lower()
    if result == 'no':
        should_continue = False
        print("Goodbye")

# END OF CODE v0.1
