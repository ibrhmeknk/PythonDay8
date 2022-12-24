alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")


def encrypt():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    word = list(text)
    for i in word:
        for k in alphabet:
            if i == k:
                index_of_word = alphabet.index(i)
                new_index_of_word = index_of_word + shift
                new_index_of_word = new_index_of_word % 26
                k = alphabet[new_index_of_word]
                new_word = []
                new_word.append(k)
                for j in new_word:
                    print(j,end = "")

def decode():
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    word = list(text)
    for i in word:
        for k in alphabet:
            if i == k:
                index_of_word = alphabet.index(i)
                new_index_of_word = index_of_word - shift
                new_index_of_word = new_index_of_word % 26
                k = alphabet[new_index_of_word]
                new_word = []
                new_word.append(k)
                for j in new_word:
                    print(j,end = "")


if direction == 'encode':
    encrypt()
else:
    decode()
