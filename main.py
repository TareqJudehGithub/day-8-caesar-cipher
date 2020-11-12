alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

# Creating a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    # Shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text:
    cipher_text = ""
    # Figuring out the index of each letter in plain_text:
    for letter in plain_text:
      position = alphabet.index(letter)
      # Shifting each letter index to their new position:
      new_position = position + shift_amount
      # New letters:
      new_letter = alphabet[new_position]
      # Coded text:
      cipher_text += new_letter
    print(cipher_text)
  

# Calling the function:
encrypt(text, shift)