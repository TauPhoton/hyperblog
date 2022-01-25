#Sustitution method crypting/decrypting script
#Tau Photon Jan 17th 2022

from string import ascii_lowercase as ascii

def encrypt(ascii):
 
    message = list(input('input message to encrypt:_ '))
    layers = int(input('aditional crypting layers: '))
    if ' ' in message:
        message.remove(' ')
    
    f_letters = [l for l in ascii if ascii.find(l) >= layers]
    f_letters = f_letters + list(ascii[:len(ascii) - len(f_letters)])
    b_letters = [l for l in ascii[::-1] if ascii[::-1].find(l) >= layers]
    b_letters = b_letters + list(ascii[:len(ascii) - len(b_letters)])

    coded = [b_letters[f_letters.index(letter)] for letter in message]
    print("".join(coded))

def decrypt(ascii):

    message = list(input('input message to decrypt:_ '))
    if ' ' in message:
        message.remove(' ')

    f_letters = [l for l in ascii]
    b_letters = [l for l in ascii[::-1]]
    decoded = [f_letters[b_letters.index(letter)] for letter in message]
    print ("".join(decoded))

def run():

    print ("""  
                encrypt[e]
                decrypt[d]
            
                """)
    menu_option = input('enter an option:_ ').lower()
    #forward_letters = list(ascii)
    #backward_letters = list(ascii[::-1])

    if menu_option == 'e':
        #encrypt(forward_letters, backward_letters)
        encrypt(ascii)
    elif menu_option == 'd':
        #decrypt(forward_letters, backward_letters)
        decrypt(ascii)
    else:
        print('terminating')

#missing: adding cryitping layers to make more secure the message
#encrypting should ask how many layers are required
#decrypting should flow until 25 iterations are made

if __name__ == '__main__':
    run()