from art import logo
from replit import clear
restart = True
while restart:

  print(logo)
  print('''
  ''')
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #Don't change the code above 👆

  def caeser(plain_text, shift_amount, cipher_direction):
    
    shift_amount = shift_amount % 25

    end_text = ""

    for char in plain_text:      
      if char in alphabet:
        position = alphabet.index(char)
        if cipher_direction == "encode":
          new_position = position + shift_amount
        elif cipher_direction == "decode":
          new_position = position - shift_amount   
        new_letter = alphabet[new_position]
        end_text += new_letter
  
      else:
        end_text += char
   
    print(f"The {cipher_direction}d text is: {end_text}")
    print('''
    ''')


  caeser(text, shift, direction)

  restart_ceaser = input("Would you like to cipher another word? (y/n) ").lower()
  if restart_ceaser == "y":
    clear()
    continue
  else:
    print("Good Bye!")
    break