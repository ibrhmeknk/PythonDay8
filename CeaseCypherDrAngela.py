from logo import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

cont = "yes"
while cont == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def ceaser(plain_text, shift_amount):
        abc = False
        cipher_text = ""
        for letter in plain_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direction == "encode":
                    new_position = position + shift_amount
                elif direction == "decode":
                    new_position = position - shift_amount
                new_position = new_position % 26
                new_letter = alphabet[new_position]
                cipher_text += new_letter
                abc = True
            elif letter not in alphabet:
                print("Just write letters please.")
                break
        if abc == True:
            print(f"The encoded text is: {cipher_text}")


    ceaser(plain_text=text, shift_amount=shift)
    cont = input("Do you want to continue?: \n")


