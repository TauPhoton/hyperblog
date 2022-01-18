#Sustitution method coder/decoder script
#Tau Photon Jan 17th 2022

import string
forward_letters = {x:y for x,y in enumerate(string.ascii_lowercase, start=1)}
# dictionary containig alphabet and number in order
backward_letters = {x:y for x,y in enumerate(string.ascii_lowercase[::-1], start=1)}
# dictionary containing alphabet and number inverse order

def encrypt(f_letters, b_letters):
    message = input('input message to encrypt:_ ').split(' ')
    message = list("".join(message))
    pass

def run():
    print ("""encrypt[e]
                decrypt[d]
            
                """)
    menu_option = input('enter an option:_ ').lower()
    #letters = list(string.ascii_lowercase[::-1])
    if menu_option == 'e':
        encrypt(forward_letters, backward_letters)
    elif menu_option == 'd':
        pass
    else:
        print('terminating')

if __name__ == '__main__':
    run()