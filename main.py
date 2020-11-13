alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above 👆

# Encrypting:

# Creating a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    
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
  

# Decrypting:

# Creating a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(plain_text, shift_amount):
 
  word = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position - shift_amount
    new_letter = alphabet[new_position]
    word += new_letter
  print(word)


# Calling functions based on direction variable input entry:
if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
else: 
  print("Bad entry.")