alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#letters are duplicated for situations such as the word zulu. 
# new_position needs to loop through letters after z but it cant if the list stops at z. 
#the index method, however, chooses the index of the 1st character of it's kind, so we're good.
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_number):
    cipher_text = ''
    for letter in original_text:
        position= alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f'The encoded text is {cipher_text}.')

def decrypt(cipher_text, shift_number):
    original_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        original_text += alphabet[new_position]
    print(f"the decoded text is {original_text}.")

if direction == "encode":
    encrypt(original_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_number=shift)
