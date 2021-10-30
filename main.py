# caesarCipher.py
#
# Python Bootcamp Day 8 - Caesar Cipher
# Usage:
#      Encrypt and decrypt code with caesar cipher. Day 8 Python Bootcamp
#
# Marceia Egler Sept 30, 2021


from art import logo
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

game = True   

def caesar(cipher:str, shift_amt:int, direction:str) -> str:  
  code = ''
  if direction == 'decode':
    shift_amt *= -1
  for i,value in enumerate(cipher):

    if value in alphabet:
      #find the index of the input in the alphabet
      answer = alphabet.index(value)
      answer += shift_amt
      #if shift_amt pushes past end of alphabet, restart
      #eg z(26) + shift(5) == 30 = (26 * 1) + 4
      alpha_loop = alphabet[answer%len(alphabet)]
      code += alpha_loop
    else:
      code += value

  print(f"The {direction}d text is {code}")  

 
print(logo)

#Allow game to continue until user says no
while game:  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(cipher=text, shift_amt=shift, direction=direction)
  play = input("Do you want to play again?\n").lower()
  
  if play == 'no':
    print(f"Thanks for playing")
    game = False 
