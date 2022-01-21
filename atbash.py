#Sustitution method coder/decoder script
#Tau Photon Jan 17th 2022

import string

def encrypt(f_letters, b_letters):

    message = list(input('input message to encrypt:_ '))
    if ' ' in message:
        message.remove(' ')
    coded = [b_letters[f_letters.index(letter)] for letter in message]
    print("".join(coded))

def decrypt(f_letters, b_letters):

    message = list(input('input message to decrypt:_ '))
    if ' ' in message:
        message.remove(' ')
    decoded = [f_letters[b_letters.index(letter)] for letter in message]
    print ("".join(decoded))

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