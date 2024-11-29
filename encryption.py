import string
user_message=input("Please enter your message\n")
user_shift=int(input("Please enter shifting number\n"))
def encrypt(message,shift):
  encrypted_message=""
  alphabet=string.ascii_lowercase
  for letter in message:
    if letter.lower() in alphabet:
      original_position=alphabet.index(letter.lower())
      new_position=(original_position+shift)%26
      encrypted_letter=alphabet[new_position]
    else:
      encrypted_message+=letter
      continue
    if letter.isupper():
      encrypted_letter=encrypted_letter.upper()
      encrypted_message+=encrypted_letter
    else:
      encrypted_message+=encrypted_letter
  print(f"Encrypted message is {encrypted_message}")
encrypt(message=user_message,shift=user_shift)
      

      