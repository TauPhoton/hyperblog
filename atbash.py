#Sustitution method coder/decoder script
#Tau Photon Jan 17th 2022

import string

def encrypt(f_letters, b_letters):

    coded = []
    message = input('input message to encrypt:_ ').split(' ')
    message = list("".join(message))

    for letter in message:
        i = f_letters.index(letter)
        coded.append(b_letters[i])
    
    #optimize if possible
    coded = "".join(coded)
    print (coded)

def decrypt(f_letters, b_letters):

    decoded = []
    message = list(input('input message to decrypt:_ '))
    for letter in message:
        i = b_letters.index(letter)
        decoded.append(f_letters[i])
    
    #optimize if possible
    decoded = "".join(decoded)
    print (decoded)

def run():

    print ("""  
                encrypt[e]
                decrypt[d]
            
                """)
    menu_option = input('enter an option:_ ').lower()
    forward_letters = list(string.ascii_lowercase)
    backward_letters = list(string.ascii_lowercase[::-1])

    if menu_option == 'e':
        encrypt(forward_letters, backward_letters)
    elif menu_option == 'd':
        decrypt(forward_letters, backward_letters)
    else:
        print('terminating')

if __name__ == '__main__':
    run()