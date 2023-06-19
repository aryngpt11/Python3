alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dir=input("Type 'encode' to encrypt ,typr 'decode' to decrypt: \n")
text=input("Type msg:\n").lower()
shift=int(input("Type the shift number: \n"))

def caesar(start_text, shift_amt, cipher_dir):
    end_text=""
    for letter in start_text:
        position=alphabet.index(letter)
        if cipher_dir=="decode":
            shift_amt=shift_amt*-1
        new_position=position+shift_amt
        end_text+=alphabet[new_position]
    print(f"The {cipher_dir}d text is {end_text}")
caesar(start_text=text,shift_amt=shift,cipher_dir=dir)


