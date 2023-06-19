alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dir=input("Type 'encode' to encrypt ,typr 'decode' to decrypt: \n")
text=input("Type msg:\n").lower()
shift=int(input("Type the shift number: \n"))

def encrypt(plain_text,Shift_amt):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position+Shift_amt
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
#encrypt(plain_text=text,Shift_amt=shift)


def decrypt(cipher_text,Shift_amt):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-Shift_amt
        plain_text+=alphabet[new_position]
    print(f"The decoded text is {plain_text}")
if dir =="encode":
    encrypt(plain_text=text,Shift_amt=shift)
elif dir=="decode":
    decrypt(cipher_text=text,Shift_amt=shift)
